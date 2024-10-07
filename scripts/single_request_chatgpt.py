"""Example of how to use the AI API client to interact with the OpenAI API."""

# Import the OpenAI API client, installed via pip. See the README for installation instructions.
from openai import OpenAI

# Import the variables from the variables.py file. All the examples use the same variables.
from .variables import prompt, gpt_role_description, temperature, base64_image

# Set the API key and model for OpenAI. Replace "your_api_key" with your OpenAI API key.
api_key = "your-api-key"
model = "gpt-4o"    # Find the model name in the OpenAI API documentation.

# Create an instance of the OpenAI API client.
client = OpenAI(api_key=api_key)

# Create a workload for the chat API.
# The workload is a list of dictionaries, where each dictionary represents a message in the conversation.
# The workload includes the user's message and the image as input. The system's role description is also included.
# See variables.py for the values of prompt, gpt_role_description, temperature, and base64_image.
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

# Call the chat API to generate a response to the user's message.
answer = client.chat.completions.create(messages=workload,
                                        model=model,
                                        temperature=temperature)

# Print the response from the API. The response is a completion object.
# Normally, you would save the response to a file or use it in your application.

# Print the content of the response.
print(answer.choices[0].message.content)

# Print the finish reason of the response. This indicates why the response generation stopped.
# If, for example,  you have insufficient token limits you'll be able to see the reason here.
print(answer.choices[0].finish_reason)

# Print the model used for the response. This is a more detailed model description than the one you set.
print(answer.model)

# Print the token usage statistics for the response.
print(answer.usage.completion_tokens)  # The number of tokens used for the completion (=answer).
print(answer.usage.prompt_tokens)      # The number of tokens used for the prompt (=question + context).
print(answer.usage.total_tokens)       # The total number of tokens used for the completion and prompt.
