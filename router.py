import sys
from logger_config import setup_logger

from commands import recipe, recipes
from commands import recipe_ingredients, recipes_kitchen
from commands import ingredient, ingredients
from commands import kitchen, errors

sys.path.append('./commands')

LOGGER = setup_logger(__name__)
COMMANDS = {'edit', 'search'} | {'recipe', 'recipes', 'ingredient', 'ingredients', 'kitchen', 'errors'}


def args_parser(args:list) -> tuple:
    """ Checks that arguments follow ['command', 'command, ..., 'search term', 'search term'] format,
         returns ([`commands`],[`search terms`]) if valid, else returns (None, None) """

    # Check all commands are valid
    # Must take in at least one command
    # Disallow duplicate commands
    # Only allow for invalid arguments (what will be 'search terms') *after* all of the valid arguments

    invalid_args_log = list()
    valid_args_log = list()

    valid = True
    for arg in args:
        LOGGER.info(f"------------ Checking '{arg}' ------------")
        if arg in COMMANDS:
            # Have to make sure that the command isn't after a potential search term 
            LOGGER.info(f"Is Command: '{arg}' *is* a command")
            if invalid_args_log:
                LOGGER.error(f"Invalid Position: '{arg}' has been entered after non-command term(s)")
                print(f"ERROR: '{arg}' command has been entered after non-command terms")
                valid = False
                break
            else:
                # Now have to make sure that the command isn't a duplicate
                if arg in valid_args_log:
                    LOGGER.error(f"Duplicate: '{arg}' was repeated")
                    print(f"ERROR: '{arg}' command is a duplicate ")
                    valid = False
                    break
                else:
                    LOGGER.info(f"Tests passed: '{arg}' is a valid additional argument")
            LOGGER.info(f"Logging: Adding '{arg}' to valid_args_log")
            valid_args_log.append(arg)
        else:
            LOGGER.info(f"Not a Command: Adding '{arg}' to invalid_args_log")
            invalid_args_log.append(arg)

    if not valid_args_log:
        LOGGER.info("Valid arguments were empty, so commands aren't valid")
        print("ERROR: No valid commands were entered, type `recipes help` if you need any guidance")
        valid = False

    if valid:
        LOGGER.info("Overall arguments were valid, returning appropriate output")
        return valid_args_log, invalid_args_log
    else:
        LOGGER.info("Arguments were empty or invalid, returning (None, None)")
        return None, None


def commands_hasher(commands:list):
    commands_hash = ""
    for command in sorted(commands):
        commands_hash += command
    LOGGER.info(f"HASH: Generated hash of '{commands_hash}'")
    return commands_hash


def validate_and_route_commands(commands:list, queries:list):
    """ Takes in commands and calls the respective function, or prints an appropriate error message """

    command_hash = commands_hasher(commands)

    functions = {
        'recipe' : recipe.info_recipe,
        'recipes' : recipes.info_recipes,
        # 'ingredient' : print("ingredient"),
        # 'ingredients' : print("ingredients"),
        # 'ingredientrecipe' : print("ERROR: Did you mean `recipes recipe ingredients"),
        # 'ingredientsrecipe' : print("recipe ingredients"),
        # 'ingredientrecipes' : print("ERROR: Did you mean `recipes recipe ingredients"),
        # 'ingredientsrecipes' : print("ERROR: Did you mean `recipes recipe ingredients"),
        # 'kitchen' : print("kitchen"),
        # 'kitchenrecipe' : print("Did you mean `kitchen recipes`?"),
        # 'kitchenrecipes' : print("kitchen recipes"),
        # 'ingredientkitchen' : print("ERROR: Did you mean `kitchen ingredients`?"),
        # 'ingredientskitchen' : print("kitchen"),
        # 'errors' : print("errors"),

        # 'editrecipe' : print("edit recipe"),
        'editrecipes' : recipes.edit_recipes,
        # 'editingredient' : print("edit ingredient"),
        # 'editingredients' : print("edit ingredients"),
        # 'editingredientrecipe' : print("ERROR: Did you mean `recipes edit recipe ingredients"),
        # 'editingredientsrecipe' : print("recipe ingredients"),
        # 'editingredientrecipes' : print("ERROR: Did you mean `recipes edit recipe ingredients"),
        # 'editingredientsrecipes' : print("ERROR: Did you mean `recipes edit recipe ingredients"),
        # 'editkitchen' : print("edit kitchen"),
        # 'editingredientkitchen' : print("Did you mean `edit kitchen ingredients`?"),
        # 'editingredientskitchen' : print("edit kitchen"),
        # 'editerrors' : print("edit errors")
    }

    try:
        command = functions[command_hash](queries)
    except KeyError:
        print("ERROR: Function was not recognised")
        LOGGER.error("ERROR: Function was not recognised")

