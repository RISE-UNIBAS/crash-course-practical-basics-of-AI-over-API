# Crash Course: Practical Basics of AI over API      
[![Pylint](https://github.com/RISE-UNIBAS/crash-course-practical-basics-of-AI-over-API/actions/workflows/pylint.yml/badge.svg)](https://github.com/RISE-UNIBAS/crash-course-practical-basics-of-AI-over-API/actions/workflows/pylint.yml)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

This repository contains the code for the Crash Course: Practical Basics of AI over API.
More information about our courses can be found on the [RISE website](https://www.rise.unibas.ch/).

## 1.) Get started

### Install Python
Check if you have Python installed on your computer by running the following command in your terminal or 
command prompt:
```sh
python --version
```
If you see a version number, you have Python installed. If you see an error message, you need to install Python.
You can download Python from the official website: https://www.python.org/downloads/
Make sure the version is 3.10 or higher.

### Option 1: Clone the repository
To download the repository, follow these steps:

1. Open your terminal or command prompt.
2. Make sure you have `git` installed. You can check by running:
    ```sh
    git --version
    ```
3. Navigate to the directory where you want to clone the repository.
4. Run the following command to clone the repository:
    ```sh
    git clone https://github.com/RISE-UNIBAS/crash-course-practical-basics-of-AI-over-API.git
    ```
5. Change into the cloned directory:
    ```sh
    cd crash-course-practical-basics-of-AI-over-API
    ```
You now have a local copy of the repository.

### Option 2: Download the repository as a ZIP file
If you don't have `git` installed, you can download the repository as a ZIP file:

1. Click on the green "Code" button in the top right corner of the repository.
2. Click on "Download ZIP".
3. Save the ZIP file to your computer.
4. Extract the ZIP file to a directory of your choice.

## 2.) Get API keys
To use the APIs in this repository, you need to get API keys from the following services:

1. OpenAI: https://platform.openai.com/
2. Anthropic: https://console.anthropic.com/
3. Google Cloud: https://aistudio.google.com/app/apikey

It is easiest to just do a web search for the respective service and "API key" to find tutorials on 
how to get the API keys.

## 3.) Install the required packages
To install the required packages, follow these steps:

1. Open your terminal or command prompt.
2. Change into the directory of the cloned repository.
3. Run the following command to install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
This will install all the required packages.

## 4.) Run the code
To run the code, follow these steps:

1. Open your terminal or command prompt.
2. Change into the directory of the cloned repository.
3. Change into the directory "scripts":
    ```sh
    cd scripts
    ```
4. Open the file to run in a text editor. Insert your API keys in the respective places.
5. Run the following command to execute the script:
    ```sh
    python <name-of-script>.py
    ```
   
## Adapt the code
You can adapt the code to your needs. Open the project in your favorite text editor or IDE (Pycharm is recommended)
and start coding. Consider the following tips:

- The code is written in Python. If you are new to Python, you can find a tutorial here: https://www.learnpython.org/ or let an LLM generate the code for you.
- The code is structured in scripts. Each script demonstrates a different API. You can run the scripts individually.
- The code is well-documented. You can find explanations for each step in the code.
- The scripts starting with `single_` demonstrate how create a single API request. The scripts starting with 
 `complete_` demonstrate how to create a complete pipeline with multiple API requests.


## Getting help
If you have any questions or need help and are affiliated with the University of Basel, please contact us at 
[RISE](https://www.rise.unibas.ch/). If you are not affiliated with the University of Basel, please directly get help in the respective API documentations:

- OpenAI: https://platform.openai.com/docs/
- Anthropic: https://docs.anthropic.com/
- Google Cloud: https://cloud.google.com/docs


## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Expanding the example

The example in this repository is a simple demonstration of how to use AI over API. You can expand the example by
adding more API requests, creating a complete pipeline, or using different APIs. You can also create your own
API requests and integrate them into the example. The possibilities are endless. Have fun coding and please create pull 
requests to share your expanded example with the community.
