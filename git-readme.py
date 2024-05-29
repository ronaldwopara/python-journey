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
url = f"https://api.github.com/repos/{username}/{repo}/contents/"
token = ""
content = get_content(repo, token, url)

prompt = f"""

**Title:** README File Creation

**Description:** Your task is to create a README file in markdown for a GitHub repository. The README file should provide essential information about the repository, including its purpose, contents, installation instructions, usage guidelines, and any other relevant details.

the name of the repository is {repo}

**Instructions:**

1. Start by providing a concise yet descriptive title for your README file.
2. Write a brief introduction or overview of the project. Explain its purpose, goals, and any relevant background information.
3. Describe the contents of the repository. List the files, directories, or resources included in the project.
4. Provide instructions for installing or setting up the project. Include any prerequisites, dependencies, or configurations needed.
5. Explain how to use or run the project. Provide examples, command-line instructions, or usage scenarios.
6. Optionally, include additional sections such as troubleshooting tips, contribution guidelines, license information, or acknowledgments.
7. Make sure to format your README file for clarity and readability. Use headings, lists, code blocks, and formatting as appropriate.

**Example:**

```
Title: Project X - README

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

```

Feel free to customize the prompt further based on your specific requirements or preferences! Let me know if you need any more assistance.

Content Of The repo 

{content}"""

print(prompt)


