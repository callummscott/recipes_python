import json
from logger_config import setup_logger

LOGGER = setup_logger(__name__)
EXIT_PHRASES = ['q', 'quit', 'cancel', 'stop', 'close', 'exit']
HELP_PHRASES = ['h', 'help']


def request_recipe_name():
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
                    with open("recipes.json", 'r') as jsonfile:
                        recipes = json.load(jsonfile)
                        recipe = recipes[response]
                        LOGGER.info(f"'{response}' found")
                        print(f"\n{response.upper()}: ")
                        print(json.dumps(recipe, indent=4))
                    repeat = False
                    break
                except KeyError:
                    LOGGER.error(f"'{response}' was not found in `recipes`")
                    print(f"ERROR: No such recipe by the name of '{response}' was found")
        else:
            print("Type 'q'/'quit' if you'd like to exit")
            # Loops again
            

def recipe(queries:list) -> None:
    """ Displays raw information about the recipe, as is stored in the .json file, not `ingredient` info.
        Takes in optional queries of `<recipe name>`. Ommitting command line argument prompts for the name 'manually'. """

    LOGGER.info('RECIPE INFO: Showing raw info for single recipe')

    if queries:
        if len(queries) == 1:
            query = queries[0]
            try:
                with open('recipes.json', 'r') as jsonfile:
                    recipes = json.load(jsonfile)
                    recipe = recipes[query]
                    LOGGER.info(f"'{query}' found")
                    print(f"\n{query.upper()}: ")
                    print(json.dumps(recipe, indent=4))
            except KeyError:
                LOGGER.error(f"'{query}' was not found in `recipes`")
                print(f"ERROR: No such recipe by the name of '{query}' was found")
        else:
            LOGGER.error("Too many arguments have been entered.")
            print("ERROR: Too many arguments have been entered. Commands must follow `recipes recipe <recipe name>` format")
    else:
        LOGGER.info('NO QUERY: Recipe name manually requested')
        request_recipe_name()


def recipes(queries:list) -> None:
    """ Lists names of all of the recipes stored in the .json file, numbered, with the option to select and view them
        by typing the corresponding number. """
    
    if (queries):
        print("ERROR: This command does not accept any recipe name queries")
    else:
        LOGGER.info('RECIPES INFO: Listing all recipes')

        with open("recipes.json", 'r') as jsonfile:
            recipes = json.load(jsonfile)

            number_to_recipe_name = {}
            print("ALL RECIPES: ")
            for index, recipe_name in enumerate(recipes):
                print(f"{index+1}: {recipe_name}")
                number_to_recipe_name[index+1] = recipe_name
            print('')

        while True:
            response = input("To inspect each recipe type its number, or type 'q' to cancel\n")
            if response.isdigit(): # Only allows "<int>", where <int> >= 0
                LOGGER.info(f"User specified: '{response}'")
                with open("recipes.json", 'r') as jsonfile:
                    recipes = json.load(jsonfile)
                    recipe_name = number_to_recipe_name[int(response)]
                    recipe_info = recipes[recipe_name]
                    print(f"{recipe_name.upper()}: ")
                    print(json.dumps(recipe_info, indent=4))
                break
            elif response in EXIT_PHRASES:
                break
            elif response in HELP_PHRASES:
                LOGGER.critical("Yet to implement 'help' command functionality")
            else:
                print("Please enter a valid input")

def router(commands:str, queries:list) -> None:
    # `remaining_commands` cannot be empty because args_parser will have already handled that
    
    cmds = set(commands)
    # `match case`` doesn't seem to work at all with sets, so resorted to elifs
    if cmds == {'recipe'}:
        recipe(queries)
    elif cmds == {'recipes'}:
        recipes(queries)
    elif cmds == {'ingredient'}:
        ingredient(cmds, queries)
    elif cmds == {'ingredients'}:
        ingredients(cmds, queries)
    elif (cmds == {'kitchen'}) or (cmds == {'kitchen', 'ingredients'}):
        kitchen(cmds, queries)
    elif cmds == {'errors'}:
        errors(cmds, queries)
    elif (cmds == {'recipe', 'ingredient'}) or (cmds == {'recipes', 'ingredient'}):
        print("ERROR: Command not recognised. Did you mean `recipes recipe ingredients`?")
    elif cmds == {'recipe', 'ingredients'}:
        #recipe_ingredients(cmds, queries)
        ...
    elif cmds == {'recipes', 'ingredients'}:
        print("ERROR: Command not recognised. Did you mean `recipes recipe ingredients`, or `recipes ingredients`?")
    elif cmds == {'kitchen', 'recipe'}:
        print("ERROR: Command not recognised. Did you mean `recipes kitchen recipes`?")
    elif cmds == {'kitchen', 'recipes'}:
        #TODO This is a complicated one, filter all recipes to show only what can be made
        #kitchen_recipes(cmds, queries)
        LOGGER.critical("Have yet to implement the complex functionality of `recipes kitchen recipes`")
    elif cmds == {'kitchen', 'ingredient'}:
        print("ERROR: Command not recognised. Did you mean `recipes kitchen ingredients`?")
    else:
        print("ERROR: Command was not recognised")
            

def ingredient(commands:list, queries:list):
    LOGGER.info('INGREDIENT INFO: Showing ingredient info')
    LOGGER.info('INGREDIENT INFO: Expecting an ingredient name after...')

def ingredients(commands:list, queries:list):
    LOGGER.info('INGREDIENTS INFO: Listing all ingredients')

def kitchen(commands:list, queries:list):
    LOGGER.info('KITCHEN INFO: Listing all kitchen contents')

def errors(commands:list, queries:list):
    LOGGER.info('ERRORS INFO: Listing all errors')

def recipe_ingredients(commands:list, queries:list):
    LOGGER.info('RECIPE INGREDIENTS INFO: Listing all recipe ingredients')
    LOGGER.info('RECIPE INGREDIENTS INFO: Expecting a recipe name after...')

def kitchen_recipes(commands:list, queries:list):
    LOGGER.info('KITCHEN RECIPES: Listing all viable recipes from kitchen ingredients')

    