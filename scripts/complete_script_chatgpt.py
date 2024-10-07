import base64
import json
import os
import re
from io import BytesIO

from PIL import Image
from openai import OpenAI

api_key = ("your_secret_api_key")
model = "gpt-4o"
section = "A"
temperature = 0.5
client = OpenAI(api_key=api_key)

for root, _, filenames in os.walk("../image_data"):
    for filename in filenames:
        if filename.endswith(".jpg"):
            print(f"Processing {filename}")
            image_id = filename.split(".")[0]

            with Image.open(os.path.join(root, filename)) as img:
                # Preserve the aspect ratio while resizing the image to fit within 1024x1492
                img.thumbnail((1024, 1492))

                # Save the resized image to a BytesIO object
                buffered = BytesIO()
                img.save(buffered, format="JPEG")

                # Convert the resized image to base64
                base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

            prompt = ('I present you an image and want you to extract every item in the list on the image.'
                      'Each list item belongs to a section and the line has the following structure: '
                      '[number]. [company], [location], [connections]. '
                      'The last part is a comma separated list to other sections. They are formatted like this '
                      '[section] [number], {section] [number]. '
                      'Please return a json list of the complete page in the described structure.'
                      f'The section of this image is "{section}", the page id is "{image_id}". You need to find the page number on the '
                      'base of the image.'
                      'An example of a valid resulting list item is:'
                      '{'
                      '  "origin": {'
                      '    "section": "A",'
                      '    "page": "11",'
                      '    "page_id": "3693659"'
                      '  },'
                      '  "number": "1", '
                      '  "company": "Abbott, Anderson & Abbott Ltd.", '
                      '  "location": "Harpenden, Herts.", '
                      '  "connections": ['
                      '     {"section": "B", "number": "123"},'
                      '     {"section": "C", "number": "13"}'
                      '  ]'
                      '}')

            workload = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                },
                {
                    "role": "system",
                    "content": "You are a precise list-reading machine and your answers are plain JSON."
                }
            ]

            answer = client.chat.completions.create(messages=workload,
                                                    model=model,
                                                    temperature=temperature)

            answer_text = answer.choices[0].message.content

            # Save the answer to a json file. The filename should be the image_id with a .json extension
            # The response from the API is a string which encloses the JSON object. We need to remove the enclosing
            # quotes to get the JSON object. ```json [data] ``` -> [data]
            pattern = "```\s*json(.*?)\s*```"
            match = re.search(pattern, answer_text, re.DOTALL)
            if match:
                # Extract the JSON content
                answer_text = match.group(1).strip()

                # Parse the JSON content into a Python object
                try:
                    answer_data = json.loads(answer_text)
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON: {e}")
                    answer_data = None

                if answer_data:
                    # Create the answers directory if it doesn't exist
                    os.makedirs("../answers", exist_ok=True)

                    # Save the answer to a JSON file
                    with open(f"../answers/{image_id}.json", "w") as json_file:
                        try:
                            json.dump(answer_data, json_file, indent=4)
                            print(f"Saved the answer for {image_id} to answers/{image_id}.json")
                        except Exception as e:
                            print(f"Failed to save the answer for {image_id} to answers/{image_id}.json")
                            print(e)
            else:
                print("No match found for the JSON content.")