import sys
import os
import json

import sys
import os
from logger_config import *

sys.path.append(os.path.abspath('../'))




LOGGER = setup_logger(__name__)

RECIPES_FILENAME = r"C:\Users\callu\Documents\Projects\Coding\python\recipes\recipes.json"
if os.path.isfile(RECIPES_FILENAME) is False:
  raise Exception("File not found")

EXIT_PHRASES = ('q', 'quit', 'cancel', 'stop', 'close', 'exit', 'cls')
HELP_PHRASES = ('h', 'help')
YES_PHRASES = ('y', 'yes', 'indeed', 'sure', 'agree')
NO_PHRASES = ('n', 'no', 'nuh uh', 'no way', 'disagree')

def clean_input(text:str):
    response = input(text)
    return response.lower().strip()

def request_recipe_name_and_print() -> None:
    repeat = True
    while repeat:
        response = clean_input("Please enter a recipe name: ")
        LOGGER.info(f"Response given was: '{response}'")
        if response:
            if response in EXIT_PHRASES:
                LOGGER.info(f"Response was an exit phrase; exiting")
                repeat = False
            else:
                try:
                    print_recipe_by_name(response)
                    repeat = False
                    break
                except KeyError:
                    LOGGER.error(f"'{response}' was not found in `recipes`")
                    print(f"ERROR: No such recipe by the name of '{response}' was found")
        else:
            print("Type 'q'/'quit' if you'd like to exit")
            # Loops again

def print_all_recipes() -> None:
    with open(RECIPES_FILENAME, 'r') as jsonfile:
        recipes = json.load(jsonfile)
        print("ALL RECIPES:")
        for recipe_name in recipes:
            print(" - " + recipe_name.title())


def print_all_recipes_with_numbered_dictionary() -> dict:
    """ Prints a numbered list of all recipes and returns a dictionary of `number` to "recipe name"s """
    
    with open(RECIPES_FILENAME, 'r') as jsonfile:
            recipes = json.load(jsonfile)

            number_to_recipe_name = {}
            print("ALL RECIPES: ")
            for index, recipe_name in enumerate(recipes):
                print(f"{index+1}: {recipe_name.title()}")
                number_to_recipe_name[index+1] = recipe_name
            print('')
    return number_to_recipe_name


def get_recipe_by_name(recipe_name:str) -> dict:
    with open(RECIPES_FILENAME, 'r') as jsonfile:
        recipes = json.load(jsonfile)
        recipe_info = recipes[recipe_name]
    return recipe_info


def print_recipe_by_name(recipe_name:str) -> None:
    recipe = get_recipe_by_name(recipe_name)
    print(f"{recipe_name.upper()}: ")
    print(json.dumps(recipe, indent=4))



