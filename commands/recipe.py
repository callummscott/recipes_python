import json
from commands.general import *

def info_recipe(queries:list) -> None:
    """ Displays raw information about the recipe, as is stored in the .json file, not `ingredient` info.
        Takes in optional queries of `<recipe name>`. Ommitting command line argument prompts for the name 'manually'. """

    LOGGER.info('RECIPE INFO: Showing raw info for single recipe')

    if queries:
        if len(queries) == 1:
            query = queries[0]
            try:
                print_recipe_by_name(query)
            except KeyError:
                LOGGER.error(f"'{query}' was not found in `recipes`")
                print(f"ERROR: No such recipe by the name of '{query}' was found")
        else:
            LOGGER.error("Too many arguments have been entered.")
            print("ERROR: Too many arguments have been entered. Commands must follow `recipes recipe <recipe name>` format")
    else:
        LOGGER.info('NO QUERY: Recipe name manually requested')
        request_recipe_name_and_print()


def edit_recipe(queries:list):
    LOGGER.info('RECIPE EDIT: Editing specific recipe')
    LOGGER.info('RECIPE EDIT: Expecting a specific recipe name...')

