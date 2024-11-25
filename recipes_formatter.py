import json
import random
import sys


def edit_recipes_json(func) -> None:
    with open('recipes.json', 'r') as file:
        data = json.load(file)

    func(data)

    with open('recipes.json', 'w') as file:
        json.dump(data, file, indent=4)

def check_response(string:str):
    check_options = {
        1 : f"You typed: \"{string}\". Are you happy with this? ",
        2 : f"You entered: \"{string}\". Are you satisfied with this answer? ",
        3 : f"You said: \"{string}\". Is this what you wanted to write? ",
        4 : f"You wrote: \"{string}\". Is that correct? ",
    }
    choice = random.choice(list(check_options.keys()))
    return check_options[choice]

def print_item_help():
    print("Type 'y' or 'yes' to accept the response")
    print("Type 'n' or 'no' to decline and change the response")
    print("Type 'next' to  the response")
    print("Type 'q' or 'quit' to leave this program")


def get_item_from_user(prompt_phrase:str) -> str:
    while True:
        user_response = input(prompt_phrase)
        response_check = input(check_response(user_response))
        match response_check.lower().strip():
            case 'y' | 'yes':
                break
            case 'n' | 'no':
                continue
            case 'q' | 'quit':
                sys.exit()
            case 's' | 'stop':
                user_exit = input("You're about the leave the program, are you sure?")
                match user_exit:
                    case 'y' | 'yes':
                        sys.exit()
                    case 'n' | 'no':
                        pass
            case _:
                print("That isn't a valid input.")
    return user_response

def get_multiple_items_from_user(prompt_phrase:str) -> list[str]:
    items = []
    while True:
        user_response = input(prompt_phrase)
        response_check = input(check_response(user_response))
        match response_check.lower().strip():
            case 'y' | 'yes':
                break
            case 'n' | 'no':
                continue
            case 'q' | 'quit':
                sys.exit()
            case 'h' | 'help':
                print_item_help()
                continue
            case _:
                print("That isn't a valid input.")
    return user_response

def add_new_recipe():
    print("Type 'h' for help with response choices")
    recipe_name = get_item_from_user("Insert a new recipe name: ")
    ingredient_name = get_item_from_user("Insert the name of an ingredient (not plural): ")
    return recipe_name, ingredient_name
                
# print(add_new_recipe())
# print_item_help()