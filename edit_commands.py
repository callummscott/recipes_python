from logger_config import setup_logger

LOGGER = setup_logger(__name__)


def router(commands:list, queries:list) -> None:

    cmds = set(commands)
    # `match case`` doesn't seem to work at all with sets, so resorted to elifs
    if cmds == {'recipe'}:
        recipe(queries)
    elif cmds == {'recipes'}:
        recipes(queries)
    elif cmds == {'ingredient'}:
        ingredient(queries)
    elif cmds == {'ingredients'}:
        ingredients(queries)
    elif (cmds == {'kitchen'}) or (cmds == {'kitchen', 'ingredients'}):
        kitchen(queries)
    elif cmds == {'errors'}:
        errors(queries)
    elif (cmds == {'recipe', 'ingredient'}) or (cmds == {'recipes', 'ingredient'}):
        print("ERROR: Command not recognised. Did you mean `recipes edit recipe ingredients`?")
    elif cmds == {'recipe', 'ingredients'}:
        #recipe_ingredients(queries)
        ...
    elif cmds == {'recipes', 'ingredients'}:
        print("ERROR: Command not recognised. Did you mean `recipes edit recipe ingredients`, or `recipes edit ingredients`?")
    elif cmds == {'kitchen', 'ingredient'}:
        print("ERROR: Command not recognised. Did you mean `recipes edit kitchen ingredients`?")
    else:
        print("ERROR: Command was not recognised")




# EDIT COMMANDS
def recipe(queries:list):
    LOGGER.info('RECIPE EDIT: Editing specific recipe')
    LOGGER.info('RECIPE EDIT: Expecting a specific recipe name...')

def recipes(queries:list):
    LOGGER.info('RECIPES EDIT: Editing all recipes')

def ingredient(queries:list):
    LOGGER.info('INGREDIENT EDIT: Editing specific ingredient')
    LOGGER.info('INGREDIENT EDIT: Expecting a specific ingredient name...')

def ingredients(queries:list):
    LOGGER.info('INGREDIENTS EDIT: Editing all ingredients')

def kitchen(queries:list):
    LOGGER.info('KITCHEN EDIT: Editing kitchen stock')

def errors(queries:list):
    LOGGER.info('ERRORS EDIT: Editing errors')
