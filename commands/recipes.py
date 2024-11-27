import json
from commands.general import *

def info_recipes(queries:list) -> None:
    """ Lists names of all of the recipes stored in the .json file, numbered, with the option to select and view them
        by typing the corresponding number. """
    
    if (queries):
        print("ERROR: This command does not accept any recipe name queries")
    else:
        LOGGER.info('RECIPES INFO: Listing all recipes')

        number_to_recipe_name = print_all_recipes_with_numbered_dictionary()

        while True:
            response = input("To inspect each recipe type its number, or type 'q' to cancel\n")
            if response.isdigit(): # Only allows "<int>", where <int> >= 0
                LOGGER.info(f"User specified: '{response}'")
                recipe_name = response
                print_recipe(recipe_name)
                break
            elif response in EXIT_PHRASES:
                break
            elif response in HELP_PHRASES:
                LOGGER.critical("Yet to implement 'help' command functionality")
            else:
                print("Please enter a valid input")


def edit_recipes(queries:list):
    LOGGER.info('RECIPES EDIT: Editing all recipes')
    if (queries):
        print("ERROR: This command does not accept any recipe name queries")
    else:
        LOGGER.info('RECIPES INFO: Listing all recipes')

        number_to_recipe_name = print_all_recipes_with_numbered_dictionary()

        while True:
            response = input("To inspect each recipe type its number, or type 'q' to cancel\n")
            if response.isdigit(): # Only allows "<int>", where <int> >= 0
                LOGGER.info(f"User specified: '{response}'")
                recipe_name = number_to_recipe_name[response]
                print_recipe(recipe_name)
                break
            elif response in EXIT_PHRASES:
                break
            elif response in HELP_PHRASES:
                LOGGER.critical("Yet to implement 'help' command functionality")
            else:
                print("Please enter a valid input")
