"""Example of how to use the AI API client to interact with the Anthropic API."""

# Import the Anthropic client, installed via pip. See the README for installation instructions.
from anthropic import Anthropic

# Import the variables from the variables.py file. All the examples use the same variables.
from .variables import prompt, base64_image

# Set the API key and model for Anthropic. Replace "your_api_key" with your Anthropic API key.
api_key = "your-api-key"
model = "claude-3-5-sonnet-20240620"   # Find the model name in the Anthropic API documentation.

# Create an instance of the Anthropic API client.
client = Anthropic(api_key=api_key)

# Create a workload for the messages API.
# The workload is a list of dictionaries, where each dictionary represents a message in the conversation.
# The workload includes the user's message and the image as input. The system's role description is also included.
# See variables.py for the values of prompt, and base64_image.
workload = [
              {
                "role": "user",
                "content":  [
                  {
                    "type": "image",
                    "source": {
                      "type": "base64",
                      "media_type": "image/jpeg",
                      "data": base64_image
                    }
                  },
                  {
                      "type": "text",
                      "text": prompt
                  }
                ],
             }
           ]

# Call the messages API to generate a response to the user's message.
# The Anthropic API requires the setting of max_tokens.
answer = client.messages.create(messages=workload,
                                model=model,
                                max_tokens=8192)

# Print the response from the API. The response is a completion object.
# Normally, you would save the response to a file or use it in your application.

# Print the content of the response.
print(answer.content[0].text)

# Print the model used for the response. This is a more detailed model description than the one you set.
print(answer.model)

# Print the stop reason of the response. This indicates why the response generation stopped.
# If, for example, you have insufficient token limits you'll be able to see the reason here.
print(answer.stop_reason)

# Print the token usage statistics for the response.
print(answer.usage.input_tokens)    # The number of tokens used for the input.
print(answer.usage.output_tokens)   # The number of tokens used for the output.
