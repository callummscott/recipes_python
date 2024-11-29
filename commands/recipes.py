import json
from commands.general import * # Omitting `commands.` leads to ModuleNotFoundError for some reason.

def info_recipes(queries:list) -> None:
    """ Lists names of all of the recipes stored in the .json file, numbered, with the option to select and view them
        by typing the corresponding number. """
    
    if (queries):
        print("ERROR: This command does not accept any recipe name queries")
    else:
        LOGGER.info('RECIPES INFO: Listing all recipes')

        number_to_recipe_name = print_all_recipes_with_numbered_dictionary()

        while True:
            response = clean_input("To inspect each recipe type its number, or type 'q' to cancel\n")
            if response.isdigit(): # Only allows "<int>", where <int> >= 0
                LOGGER.info(f"User specified: '{response}'")
                recipe_name = number_to_recipe_name[int(response)]
                print_recipe_by_name(recipe_name)
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

        print("OPTIONS:")
        options = {'add':add_recipe, 'remove':remove_recipe, 'change':change_recipe, 'reset':reset_recipes}
        for option in options:
            print(f"> {option}")

        while True:
            
            response = clean_input("First, type one of the command options above:\n")
            if response in options:
                options[response]()
                break
            elif response in EXIT_PHRASES:
                break
            elif response in HELP_PHRASES:
                LOGGER.critical("Yet to implement 'help' command functionality")
                break
            else:
                print("ERROR: Response was invalid")


def add_recipe():
   
    print('')
    while True:

        response = clean_input("Please enter your new recipe name: ")
        if not response:
            print("ERROR: No response was given")
            break
        if response in EXIT_PHRASES:
            break
        elif response in HELP_PHRASES:
            print(" - Type in your new recipe name")
            print(" - Type 'q' or 'quit' to exit")

        check = clean_input(f"The new recipe name will be '{response.upper()}'. Press enter to continue, 'n' to retry, or type 'h' or 'help'. ")
        if check:
            if check in NO_PHRASES:
                continue # Is there a difference between this and pass/...?
            elif check in EXIT_PHRASES:
                break
            elif check in HELP_PHRASES:
                print(" - Type nothing and press enter in order to accept your choice.")
                print(" - Type 'n' or 'no' to try again.")
                print(" - Or type 'q' or 'quit' to exit.")
                break
        else: # i.e. Press 'enter'
            with open(RECIPES_FILENAME, 'r') as jsonfile:
                recipes = json.load(jsonfile)
            recipes[response] = dict()
            with open(RECIPES_FILENAME, 'w') as jsonfile:
                json.dump(recipes, jsonfile, indent=4, separators=(',', ' : '))
            break


def remove_recipe():
    print('')
    print("REMOVING")
    ...


def change_recipe():
    print("CHANGING")
    ...


def reset_recipes():
    print("RESETTING")
    ...
