import json
from logger_config import setup_logger



LOGGER = setup_logger(__name__)
EXIT_PHRASES = ['q', 'quit', 'cancel', 'stop', 'close', 'exit']
HELP_PHRASES = ['h', 'help']





def request_recipe_name_and_print() -> None:
    repeat = True
    while repeat:
        response = input("Please enter a recipe name: ").strip().lower()
        LOGGER.info(f"Response given was: '{response}'")
        if response:
            if response in EXIT_PHRASES:
                LOGGER.info(f"Response was an exit phrase; exiting")
                repeat = False
            else:
                try:
                    print_recipe(response)
                    repeat = False
                    break
                except KeyError:
                    LOGGER.error(f"'{response}' was not found in `recipes`")
                    print(f"ERROR: No such recipe by the name of '{response}' was found")
        else:
            print("Type 'q'/'quit' if you'd like to exit")
            # Loops again


def print_all_recipes_with_numbered_dictionary() -> dict:
    """ Prints a numbered list of all recipes and returns a dictionary of `number` to "recipe name"s """

    with open("recipes.json", 'r') as jsonfile:
            recipes = json.load(jsonfile)

            number_to_recipe_name = {}
            print("ALL RECIPES: ")
            for index, recipe_name in enumerate(recipes):
                print(f"{index+1}: {recipe_name}")
                number_to_recipe_name[index+1] = recipe_name
            print('')
    return number_to_recipe_name


def print_recipe(recipe_name:str) -> None:
    with open("recipes.json", 'r') as jsonfile:
        recipes = json.load(jsonfile)
        recipe_info = recipes[recipe_name]
        print(f"{recipe_name.upper()}: ")
        print(json.dumps(recipe_info, indent=4))