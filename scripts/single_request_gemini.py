"""Example of how to use the AI API client to interact with the Gemini API."""

# Import the GenerativeAI client, installed via pip. See the README for installation instructions.
import google.generativeai as genai

# Import the variables from the variables.py file. All the examples use the same variables.
from .variables import prompt, img_path

# Set the API key and model for GenerativeAI. Replace "your_api_key" with your GenerativeAI API key.
api_key = "your-api-key"
model = "gemini-1.5-flash"

# Configure the GenerativeAI client with your API key.
genai.configure(api_key=api_key)

# Create an instance of the GenerativeAI API client.
model = genai.GenerativeModel(model)

# Upload the image file to the GenerativeAI API.
image_file = genai.upload_file(path=img_path)

# Call the generate_content API to generate a response to the user's message.
response = model.generate_content([prompt, image_file])

# Print the response from the API. The response is a completion object.
print(response.text)

# Print the token usage statistics for the response.
print(response.usage_metadata.prompt_token_count)       # The number of tokens used for the prompt.
print(response.usage_metadata.candidates_token_count)   # The number of tokens used for the candidates.
print(response.usage_metadata.total_token_count)        # The total number of tokens used for the completion.
