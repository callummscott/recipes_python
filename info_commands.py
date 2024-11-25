import json
from logger_config import setup_logger

LOGGER = setup_logger(__name__)
EXIT_PHRASES = ['q', 'quit', 'cancel', 'stop', 'close', 'exit']

def get_recipe_name(query:str):
    with open("recipes.json", 'r') as jsonfile:
                recipes = json.load(jsonfile)
                for recipe_name in recipes:
                    if recipe_name == query:
                        LOGGER.info(f"'{recipe_name}' == '{query}' found")
                        print(f"\n{recipe_name.upper()}: ")
                        print(json.dumps(recipes[recipe_name], indent=4))
                        # print(recipes[response])
                        repeat = False # Not redundant
                        break
                    else:
                        LOGGER.error(f"{query} was not found in `recipes`")
                if repeat:
                    LOGGER.info(f"Not '{query}' was found")
                    print(f"No such recipe was found by the name: {query}")

def request_recipe_name():
    repeat = True
    while repeat:
        response = input("Please enter a recipe name: ").strip().lower()
        LOGGER.info(f"Response given was: '{response}'")
        if response:
            if response in EXIT_PHRASES:
                LOGGER.info(f"Response was an exit phrase; exiting")
                repeat = False # redundant
                break
            with open("recipes.json", 'r') as jsonfile:
                recipes = json.load(jsonfile)
                for recipe_name in recipes:
                    if recipe_name == response:
                        LOGGER.info(f"'{recipe_name}' == '{response}' found")
                        print(f"\n{recipe_name.upper()}: ")
                        print(json.dumps(recipes[recipe_name], indent=4))
                        # print(recipes[response])
                        repeat = False # Not redundant
                        break
                    else:
                        LOGGER.error(f"{response} was not found in `recipes`")
                if repeat:
                    LOGGER.info(f"Not '{response}' was found")
                    print(f"No such recipe was found by the name: {response}")
                    print("Type 'q'/'quit' if you'd like to stop")
        else:
            print("Please enter a recipe name")
            

def recipe(command_ids:str, queries:list) -> None:
    LOGGER.info('RECIPE INFO: Showing info for single recipe')

    if not command_ids:
        if (queries) and (len(queries) == 1):
            get_recipe_name(queries[0])
        elif (queries) and (len(queries) > 1):
            print("'recipe' command only takes 1 argument")
        else:
            LOGGER.info('NO QUERY: Recipe name manually requested')
            request_recipe_name()
    else:
        LOGGER.critical("Extra command functionality not implemented yet")


def recipes(command_ids:str, queries:list) -> None:
    LOGGER.info('RECIPES INFO: Listing all recipes')
    print("ALL RECIPES: ")
    with open("recipes.json", 'r') as jsonfile:
        recipes = json.load(jsonfile)
        for index, recipe_name in enumerate(recipes):
            print(f"{index+1}: {recipe_name}")
    while True:
        response = input("\nTo inspect each recipe, type its number, or type 'q'/'quit' to cancel\n")
        if response.isdigit():
            LOGGER.info(f"User specified: '{response}'")
            break
        elif response in EXIT_PHRASES:
            break
        else:
            print("Please enter a valid input")

def ingredient(command_ids:str, queries:list):
    LOGGER.info('INGREDIENT INFO: Showing ingredient info')
    LOGGER.info('INGREDIENT INFO: Expecting an ingredient name after...')

def ingredients(command_ids:str, queries:list):
    LOGGER.info('INGREDIENTS INFO: Listing all ingredients')

def kitchen(command_ids:str, queries:list):
    LOGGER.info('KITCHEN INFO: Listing all kitchen contents')

def errors(command_ids:str, queries:list):
    LOGGER.info('ERRORS INFO: Listing all errors')
