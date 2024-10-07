"""This script uses the Google Gemini API to process images and extract information from them. The script reads
images from a directory, resizes them, and sends them to the API along with a prompt. The API generates a response
containing the extracted information in JSON format. The script saves the extracted information to a JSON file with
the same name as the image file. The script processes multiple images in a batch."""

# Import the required libraries
import json
import os
import re
import time

# Import the Google Gemini client
import google.generativeai as genai

# Save the start time, set the image and output directories
start_time = time.time()
total_files = 0
total_in_tokens = 0
total_out_tokens = 0
input_cost_per_mio_in_dollars = 2.5
output_cost_per_mio_in_dollars = 10

image_directory = "../image_data"
output_directory = "../answers/google"

# Clear the output directory
for root, _, filenames in os.walk(output_directory):
    for filename in filenames:
        os.remove(os.path.join(root, filename))

# Set the API key, model, section, and temperature
api_key = "your-api-key"
model = "gemini-1.5-flash"
section = "A"
temperature = 0.5

# Configure the GenerativeAI client with your API key.
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model)

# Process each image in the image_data directory
for root, _, filenames in os.walk(image_directory):
    file_number = 1
    total_files = len(filenames)
    for filename in filenames:
        if filename.endswith(".jpg"):
            print("----------------------------------------")
            print(f"> Processing file ({file_number}/{total_files}): {filename}")
            image_id = filename.split(".")[0]

            # Create the prompt for the model
            print("> Sending the image to the API and requesting answer...", end=" ")
            prompt = ('I present you an image and want you to extract every item in the list on the image.'
                      'Each list item belongs to a section and the line has the following structure: '
                      '[number]. [company], [location], [connections]. '
                      'The last part is a comma separated list to other sections. They are formatted like this '
                      '[section] [number], {section] [number]. '
                      'Please return a json list of the complete page in the described structure.'
                      f'The section of this image is "{section}", the page id is "{image_id}". '
                      f'You need to find the page number on the base of the image.'
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

            image_file = genai.upload_file(path=os.path.join(root, filename))

            answer = model.generate_content([prompt, image_file])
            print("Done.")

            # Extract the answer from the response
            answer_text = answer.text
            print("> Received an answer from the API. Token cost (in/out):",
                  answer.usage_metadata.prompt_token_count, "/",
                  answer.usage_metadata.candidates_token_count)
            total_in_tokens += answer.usage_metadata.prompt_token_count
            total_out_tokens += answer.usage_metadata.candidates_token_count

            print("> Processing the answer...")
            # Save the answer to a json file. The filename should be the image_id with a .json extension
            # The response from the API is a string which encloses the JSON object. We need to remove the enclosing
            # quotes to get the JSON object. ```json [data] ``` -> [data]
            pattern = r"```\s*json(.*?)\s*```"
            match = re.search(pattern, answer_text, re.DOTALL)
            if match:
                # Extract the JSON content
                answer_text = match.group(1).strip()

                # Parse the JSON content into a Python object
                try:
                    answer_data = json.loads(answer_text)
                except json.JSONDecodeError as e:
                    print(f"> Failed to parse JSON: {e}")
                    answer_data = None

                if answer_data:
                    # Create the answers directory if it doesn't exist
                    os.makedirs(output_directory, exist_ok=True)

                    # Save the answer to a JSON file
                    with open(f"{output_directory}/{image_id}.json", "w", encoding="utf-8") as json_file:
                        json.dump(answer_data, json_file, indent=4)
                        print(f"> Saved the answer for {image_id} to {output_directory}/{image_id}.json")

            else:
                print("> No match found for the JSON content.")

            # File complete: Increment the file number
            file_number += 1
            print("> Processing the answer... Done.")

# Calculate and print the total processing time
end_time = time.time()
total_time = end_time - start_time
print("----------------------------------------")
print(f"Total processing time: {total_time:.2f} seconds")
print(f"Total token cost (in/out): {total_in_tokens} / {total_out_tokens}")
print(f"Average token cost per image: {total_out_tokens / total_files}")
print(f"Total cost (in/out): ${total_in_tokens / 1e6 * input_cost_per_mio_in_dollars:.2f} / "
      f"${total_out_tokens / 1e6 * output_cost_per_mio_in_dollars:.2f}")
print("----------------------------------------")
