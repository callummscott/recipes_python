import json

# Example:
test = {'meta': {'url': 'N/A', 'time': 'lunch | breakfast | snack', 'servings': '1', 'keywords': 'peanut butter | toast | banana | protein'}, 'primary': {'banana': '1', 'bread slice': '1-2', 'peanut butter': '3tbsp'}, 'secondary': {'optional': {'honey': 'to taste'}}}

# Pseudocode:
# 0. Print json brackets, newline, tab
# 1. Print first key in json, formatted to match its type
# 2. Print ' : '
# 3. Dependending upon the `type` of the value, print '{' or '[' or ' " ' or whateve, newline, tab
# 4. If it's a dictionary, do the same again, if it's a list, do the same minus the colons, if it's a string, print the string


def start_item(key, value):

    # Handing keys
    if isinstance(key, str):
        print(f'"{key}" : ', end='')
    else:
        print(f"{key} : ", end='')

    # Handling values
    if isinstance(value, dict):
        print("{\n")
        # Print contents
        print("")
    elif isinstance(value, list):
        print("[\n")
    elif isinstance(value, str):
        print(f'"{value}')
    else:
        print(value)

def print_dictionary(dictionary:dict):
    ...

for key, value in test.items():
    start_item(key, value)