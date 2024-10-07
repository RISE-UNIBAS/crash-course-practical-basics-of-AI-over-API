"""Example of how to use the AI API client to interact with the Gemini API."""
from openai import OpenAI
from variables import prompt, gpt_role_description, temperature, base64_image

# Set the API key and model for OpenAI
api_key = ("your-api-key")
model = "gpt-4o"


client = OpenAI(api_key=api_key)

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
                   "content": gpt_role_description
               }
           ]

answer = client.chat.completions.create(messages=workload,
                                        model=model,
                                        temperature=temperature)

print(answer.choices[0].message.content)
print(answer.choices[0].finish_reason)
print(answer.model)
print(answer.usage.completion_tokens)
print(answer.usage.prompt_tokens)
print(answer.usage.total_tokens)
