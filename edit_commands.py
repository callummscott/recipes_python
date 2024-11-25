from logger_config import setup_logger

LOGGER = setup_logger(__name__)

# EDIT COMMANDS
def recipe(command_ids:str, queries:list):
    LOGGER.info('RECIPE EDIT: Editing specific recipe')
    LOGGER.info('RECIPE EDIT: Expecting a specific recipe name...')

def recipes(command_ids:str, queries:list):
    LOGGER.info('RECIPES EDIT: Editing all recipes')

def ingredient(command_ids:str, queries:list):
    LOGGER.info('INGREDIENT EDIT: Editing specific ingredient')
    LOGGER.info('INGREDIENT EDIT: Expecting a specific ingredient name...')

def ingredients(command_ids:str, queries:list):
    LOGGER.info('INGREDIENTS EDIT: Editing all ingredients')

def kitchen(command_ids:str, queries:list):
    LOGGER.info('KITCHEN EDIT: Editing kitchen stock')

def errors(command_ids:str, queries:list):
    LOGGER.info('ERRORS EDIT: Editing errors')
