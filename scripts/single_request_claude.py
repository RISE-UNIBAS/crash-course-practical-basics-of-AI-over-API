"""Example of how to use the AI API client to interact with the Gemini API."""
from anthropic import Anthropic
from variables import prompt, base64_image

# Set the API key and model for Anthropic
api_key = "your-api-key"

client = Anthropic(api_key=api_key)

answer = client.messages.create(messages=[
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
                                ],
                                model="claude-3-5-sonnet-20240620",
                                max_tokens=4096*2)

print(answer.content[0].text)
print(answer.model)
print(answer.stop_reason)
print(answer.usage.input_tokens)
print(answer.usage.output_tokens)
