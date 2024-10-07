"""Example of how to use the AI API client to interact with the Gemini API."""
import google.generativeai as genai
from variables import prompt, img_path

api_key = "your-api-key"
model = "gemini-1.5-flash"

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model)
image_file = genai.upload_file(path=img_path)

response = model.generate_content([prompt, image_file])

print(response.text)
print(response.usage_metadata.prompt_token_count)
print(response.usage_metadata.candidates_token_count)
print(response.usage_metadata.total_token_count)
