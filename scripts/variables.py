"""Common variables for all examples in this repository."""
import base64
from io import BytesIO
from PIL import Image

# SINGLE IMAGE: Load a single image from the repository
# (used in single_request_*.py)
img_path = "../image_data/3693659.jpg"
# Open the image with PIL (Python Imaging Library)
with Image.open(img_path) as img:
    # Preserve the aspect ratio while resizing the image to fit within 1024x1492
    # Change this according to the model's requirements and your needs
    img.thumbnail((1024, 1492))

    # Save the resized image to a BytesIO object
    buffered = BytesIO()
    img.save(buffered, format="JPEG")

    # Convert the resized byteIO object to base64
    # The image is now saved as a string in base64 format and can be used in the API request
    base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

# COMMON VARIABLES: Used in all examples

# Temperature parameter for the model. Temperature controls the randomness of the model's output.
temperature = 0.5

# The example sources used in the examples use the following prompt and role description.
# 'section' and 'page_id' are placeholders that are used in the single_request_*.py examples.
# Thy are replaced with the actual values in the complete_script_*.py examples.
section = "A"           # The section of the image in the source book (A, B, or C)
page_id = "3693659"     # The page ID of the image. Stems from e-manuscripta.ch

# The prompt for the model. This is the text that the model will use to generate the response.
prompt = ('I present you an image and want you to extract every item in the list on the image.'
          'Each list item belongs to a section and the line has the following structure: '
          '[number]. [company], [location], [connections]. '
          'The last part is a comma separated list to other sections. They are formatted like this '
          '[section] [number], {section] [number]. '
          'Please return a json list of the complete page in the described structure.'
          f'The section of this image is "{section}", the page id is "{page_id}". '
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

# The role description for the model. This is the role that the model will assume when generating the response.
gpt_role_description = "You are a precise list-reading machine and your answers are plain JSON."
