from logger_config import setup_logger

LOGGER = setup_logger(__name__)

# EDIT COMMANDS
def recipe(commands:str, queries:list):
    LOGGER.info('RECIPE EDIT: Editing specific recipe')
    LOGGER.info('RECIPE EDIT: Expecting a specific recipe name...')

def recipes(commands:str, queries:list):
    LOGGER.info('RECIPES EDIT: Editing all recipes')

def ingredient(commands:str, queries:list):
    LOGGER.info('INGREDIENT EDIT: Editing specific ingredient')
    LOGGER.info('INGREDIENT EDIT: Expecting a specific ingredient name...')

def ingredients(commands:str, queries:list):
    LOGGER.info('INGREDIENTS EDIT: Editing all ingredients')

def kitchen(commands:str, queries:list):
    LOGGER.info('KITCHEN EDIT: Editing kitchen stock')

def errors(commands:str, queries:list):
    LOGGER.info('ERRORS EDIT: Editing errors')
