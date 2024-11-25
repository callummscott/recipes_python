import json

class recipe:
    def __init__(self, name):
        try:
            self.data = recipes[name]
        except KeyError as e:
            raise e('Please input a valid name for a recipe')
        
        self.name = name
        self.primary = self.data['primary']

        try: self.secondary = self.data['secondary']
        except KeyError: self.secondary = {'N/A' : 0}
        try: self.required = self.secondary['required']
        except KeyError: self.required = {'N/A' : 0}
        try: self.optional = self.secondary['optional']
        except KeyError: self.optional = {'N/A' : 0}
    
    def __str__(self):
        return str(self.data)



def joined_ingredient_parser(ingredients:str) -> set:
    """ Converts any "a | b" ingredient string into an {a, b} set used for
     checking if ingredient_prices.json has values for all potential ingredients. """
    
    split_ingredients = ingredients.split('|')
    output = set()
    for ingredient in split_ingredients:
        output.add(ingredient.strip())
    return output


def list_all_recipes() -> set:
    """ Returns a set of all the names for the recipes stored in `recipe.json`. """
    return {key for key in recipes}


def list_specific_recipe_potential_ingredients(recipe_name:str) -> set:
    """ Returns a set of all ingredients mentioned at all in the recipe,
    this is useful for checking if all potential ingredients have prices. """

    current = recipe(recipe_name)
    total_ingredients = current.primary | current.required | current.optional

    recipe_ingredients = set()
    for ingredient_key in total_ingredients:
        parsed_ingredients = joined_ingredient_parser(ingredient_key)
        recipe_ingredients = recipe_ingredients.union(parsed_ingredients)

    return recipe_ingredients


def list_specific_recipe_required_ingredients(recipe_name:str) -> set:
    """ Returns a set of all the ingredients, where substitutable ones are kept as a "a | b" string,
     useful for checking if you have enough ingredients to cook the recipe. """
    
    current = recipe(recipe_name)
    total_ingredients = current.primary | current.required | current.optional

    recipe_ingredients = set()
    for ingredient_key in total_ingredients:
        parsed_ingredients = joined_ingredient_parser(ingredient_key)
        recipe_ingredients = recipe_ingredients.union(parsed_ingredients)

    return recipe_ingredients


def list_all_potential_recipe_ingredients() -> set:
    """ Lists as a set all of the potential ingredients involved in all recipes. 
    used to see if the prices for all ingredients are stored. """

    possible_ingredients = set()
    for recipe_name in recipes:
        test = list_specific_recipe_potential_ingredients(recipe_name)
        possible_ingredients = possible_ingredients.union(test)
    
    possible_ingredients.remove('N/A')
    return possible_ingredients


def get_recipe_times(recipe:str):
    time = recipes[recipe]['meta']['time']
    return time


with open('recipes.json', encoding='utf-8') as file:
    recipes = json.load(file)


# print(sorted(list_all_recipes()))
# print(list_all_potential_recipe_ingredients())