# My Code Assistant
## Description

This repository is designed to integrate Large Language Model (LLM), specifically [PaLM API](https://developers.generativeai.google/) as a developer assistant, into your coding development process. It can serve various functions such as generating code, fixing code, creating documentation for your code, and explaning complex codes. The library is designed to be easy to use so that one can keep his code locally without having to do copy & paste their private code to public such as ChatGPT. In a nutshell, you bring LLM into your IDE or local computer while keeping your code with you.

## Installation

1. ```!pip install -q google.generativeai```
1. Download this main repository
2. Get a free [PaLM API KEY](https://developers.generativeai.google/).
3. Put the API key in ```config_api.py``` =>
    ```PALM_API_KEY = 'YOUR API KEY' ```
**Note** : By default ```config_api.py``` is in .gitignore to prevent your PaLM API KEY to be pushed to Github



## Usage example

The following example shows how to use the library to generate code to create a list of odd numbers:

### 1. Import MyCodeAssistant
**NOTE** : mind the path of the downloaded folder of this repo
```
Import MyCodeAssistant from code_assistant
```
### 2. Set up the prompts and Run
```
priming = "You are an expert at writing clear, concise, Python code. Please create code for the following case :"
question = "Create a list of odd numbers"
decorator = "Insert comments for each line of code and end explanation in bullet points"

assistant = MyCodeAssistant()
my_code = assistant.generate_code(priming, question, decorator)
print(my_code)

```

### Output
```python
## Create a list of odd numbers from 1 to 100
odd_numbers = [number for number in range(1, 101) if number % 2 != 0]

## Print the list of odd numbers
print(odd_numbers)

## Explanation:
# The `range()` function creates a list of numbers from a starting point to an ending point.
# The `if` statement checks if each number in the list is odd by checking if the number is divisible by 2.
# The `%` operator returns the remainder of a division operation.
# If the remainder is 0, then the number is divisible by 2 and is not odd.
# If the remainder is not 0, then the number is not divisible by 2 and is odd.
# The `for` loop iterates over the list of numbers and adds each odd number to the `odd_numbers` list.
# The `print()` function prints the list of odd numbers.
```

## Contact
If you have any questions or would like to collaborate for anything related to AI or LLM, feel free to reach me at
ihshan.jaka@ambit.ai or [my website](https://www.igumilar.com/).

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).
