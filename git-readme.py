#This code serves the purpose of creating a prompt for a chatbot. The propmt tells the chatbot to create a README files in github repos

import requests


def get_content(repo, url, token, indent_lvl=0):
 prompt = ""  # The final prompt for the chatbot
 headers = {"Authorization": f"token {token}"}

 response = requests.get(url, headers=headers)
 contents = response.json()

 base_files = ""
 directory_structure = ""

 # Structuring the prompt
 for item in contents:
   indent = " " * (indent_lvl * 2)  # Indentation for nested directories

   if item["type"] == "file":
    base_files += f"{indent} File: {item['name']}\n \n \n"

   elif item["type"] == "dir":
    directory_structure += f"{indent} Directory: {item['name']}\n \n \n"
    directory_structure += get_content(repo, item["url"], token, indent_lvl + 1)  # Recursively call the function to get the files and directories inside other directories
 
 prompt += directory_structure + base_files
 return prompt

repo = ""
username = ""
token = ""
url = f"https://api.github.com/repos/{username}/{repo}/contents/"
content = get_content(repo, url, token)

prompt = f"""

**Title:** README File Creation

**Description:** Your task is to create a README file in markdown for a GitHub repository. I repeat in markdown. The README file should provide essential information about the repository, including its purpose, contents, installation instructions, usage guidelines, and any other relevant details.

the name of the repository is {repo}

**Instructions:**

1. Start by providing a concise yet descriptive title for your README file.
2. Write a brief introduction or overview of the project. Explain its purpose, goals, and any relevant background information.
3. Describe the contents of the repository. List the files, directories, or resources included in the project.
4. Provide instructions for installing or setting up the project. Include any prerequisites, dependencies, or configurations needed.
5. Explain how to use or run the project. Provide examples, command-line instructions, or usage scenarios.
6. Optionally, include additional sections such as troubleshooting tips, contribution guidelines, license information, or acknowledgments.
7. Make sure to format your README file for clarity and readability. Use headings, lists, code blocks, and formatting as appropriate.
8. Dont render the README file that youve made, just output it in raw mardown without rendering
9. I repeat, Dont render the README file that youve made, just output it in raw mardown code without rendering. When you render the markdown i am unable to copy it directly, so dont render it.

**Example:**

```
README - Project X

Description:
Welcome to Project X! This repository contains the source code and resources for an exciting new project aimed at revolutionizing the world of AI-driven chatbots.

Contents:
- main.py: Python script for running the chatbot engine.
- data/: Directory containing training data and pre-trained models.
- README.md: This file providing essential information about the project.

Installation:
To set up Project X on your local machine, follow these steps:
1. Clone the repository: git clone https://github.com/your-username/project-x.git
2. Navigate to the project directory: cd project-x
3. Install dependencies: pip install -r requirements.txt

Usage:
To run Project X, execute the following command:
python main.py

Contributing:
We welcome contributions from the community! If you'd like to contribute to Project X, please follow these guidelines:
- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and submit a pull request with a clear description of your changes.
- Be sure to test your changes thoroughly and adhere to our coding standards.

License:
Project X is licensed under the MIT License. See the LICENSE file for details.




**example 2**
# README - Magic 8-Ball and Shipping Calculator

## Introduction
Welcome to the Magic 8-Ball and Shipping Calculator repository! This repository contains two Python scripts: one for a Magic 8-Ball game and another for a simple shipping calculator. These scripts are designed to provide fun and utility, respectively, in Python programming.

## Contents
- **magic-8ball.py**: Python script for playing the Magic 8-Ball game.
- **shipping.py**: Python script for calculating shipping costs.

## Installation
To use the scripts in this repository, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/magic-8ball-shipping-calculator.git`
2. Navigate to the project directory: `cd magic-8ball-shipping-calculator`

## Usage
### Magic 8-Ball
1. Open a terminal or command prompt.
2. Navigate to the directory containing `magic-8ball.py`.
3. Run the script using Python: `python magic-8ball.py`.
4. Follow the prompts to ask the Magic 8-Ball a question and receive an answer.

### Shipping Calculator
1. Open a terminal or command prompt.
2. Navigate to the directory containing `shipping.py`.
3. Run the script using Python: `python shipping.py`.
4. Follow the prompts to enter package dimensions and shipping information.
5. The script will calculate the shipping cost based on the provided information.

## Contribution
Contributions to this repository are welcome! If you'd like to contribute, please follow these guidelines:
- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and submit a pull request with a clear description of your changes.
- Be sure to test your changes thoroughly.

## License
This repository is licensed under the MIT License. See the LICENSE file for details.

Note: Let your output only be in markdown, to make copying easier

Content Of The repo 

{content}"""

print(prompt)


