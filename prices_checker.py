import json
from logger_config import setup_logger
import re
from recipes_parser import *
from unit_converter import masses, volumes, unit_pattern

########################################################################################################################
########################################################################################################################

with open('ingredient_prices.json', encoding='utf-8') as file:
        prices = json.load(file)

def all_recipe_price_validator() -> set:
    """ Used to check if there are any potential ingredients from `recipes.json` that haven't got price information stored. """

    priced_ingredients = set(item for item in prices)
    
    missing_prices = set()
    all_potential_ingredients = list_all_potential_recipe_ingredients()
    for ingredient in all_potential_ingredients:
        if ingredient not in priced_ingredients:
            missing_prices.add(ingredient)

    print(f"There are {len(missing_prices)} missing prices:")
    return missing_prices


def specific_recipe_price_validator(recipe_name:str) -> set:
    """ Used to check whether the `ingredient_prices.json` has documented all of the relevant ingredients required for a given recipe. """

    #TODO Currently is saying that you need prices for every single potential ingredient, rather than showing for example 'basil leaves | mint leaves'
    #TODO   It would have to actually separate the 'a | b | c' strings, remove any ingredients that do have prices, and then if necessary, re-combine them. 
    
    current_ingredients = list_specific_recipe_required_ingredients(recipe_name)
    missing_prices = set()
    for ingredient in current_ingredients:
        if ingredient not in prices:
            missing_prices.add(ingredient)
    print(f"There are {len(missing_prices)} missing prices")
    if 'N/A' in missing_prices: (missing_prices.remove('N/A'), logger.info('Removing reference to N/A'))
    return not missing_prices


def quantity_validator(quantity:str) -> bool:
    if not isinstance(quantity, str):
        return False
    try:
        number = float(quantity)
        return (number > 0)
    except ValueError:
        if (match:=re.match(unit_pattern, quantity)) and (match.group(2) in (masses | volumes)):
            return True
    return False

def value_validator(value:str) -> bool:
    if not isinstance(value, str):
        return False
    value_pattern = r"^£(\d+(\.\d{2})?)$"
    if match := re.match(value_pattern, value):
        return True
    return False

def missing_price_information_flagger():
    """ Scours `ingredient_prices.json` looking for missing values. """

    missing_information = list()
    for ingredient in prices:
        # Check if there are no stores listed for the ingredient
        stores_to_quantities = prices[ingredient] # e.g. {"LIDL":{...}, "ALDI":{...}, "ASDA":{...}}
        if len(stores_to_quantities) == 0:
            missing_data_label = f"prices > {ingredient} > MISSING"
            missing_information.append(missing_data_label)

        # Then check if there are no quantities listed for each store
        for store, quantities in stores_to_quantities.items():
            quantities_to_values = quantities
            if len(quantities_to_values) == 0: # i.e. no quantities (e.g. "450g", "2L")
                missing_data_label = f"{ingredient} > {store} > MISSING"
                missing_information.append(missing_data_label)

            # Then check if the quantities are valid 
            for quantity, value in quantities_to_values.items():
                if not quantity_validator(quantity):
                    missing_data_label = f"{ingredient} > {store} > "
                    if not quantity:
                        missing_data_label += "MISSING > "
                    else:
                        missing_data_label += "ERROR > "
                else:
                    missing_data_label = f"{ingredient} > {store} > {quantity} > "
                if not value_validator(value):
                    if not value:
                        missing_data_label += "MISSING"
                    else:
                        missing_data_label += "ERROR"
                else:
                    missing_data_label += value
                if (not value_validator(value)) or (not quantity_validator(quantity)):
                    missing_information.append(missing_data_label)
    return sorted(missing_information)

def get_cheapest_specific_recipe_price(recipe_name:str) -> int:
    """ Returns cheapest price of recipe given ingredients are priced. """
    # Check that all constituent ingredients have prices first, raise Error if not?
    recipe_is_valid = specific_recipe_price_validator(recipe_name)
    if not recipe_is_valid:
        raise AttributeError('Prices of ingredients incomplete')
    
    # Get all ingredients

if __name__ == "__main__":
    logger = setup_logger(__name__)