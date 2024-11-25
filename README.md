# CLI Python Recipe Manager

## Overview
This program is intended to be used in the CLI with the command `recipes`. The following features are not yet fully implemented.
You can use it to store the ingredients for your favourite recipes, seach for recipes, calculate how much you have to buy for a given number of servings,
calculate the prices of recipes, generate shopping lists, and much more.

By inputting the contents of your kitchen, you can find which of your recipes you can make without having to think, and you can calculate what would be cheapest to shop for given what you already have available.

## Guide

There are 6 'noun' keywords, `recipe`, `recipes`, `ingredient`, `ingredients`, `kitchen`, and `errors`, 2 explicit 'verb' keywords, `edit` and `search`, and you can follow it up with various query terms.

By intuitively combining these keywords without repetition, you can access various features of the program:
- `recipes recipes`: Displays all of the recipes that you have saved in a numbered list. You are prompted for a numerical input to then view any of these recipes.
- `recipes recipe *<recipe name>`: Jumps straight to displaying a specific recipe. Omitting the name as an argument prompts you to input one.
- `recipes recipe ingredients *<recipe name> *<serving size>`: Displays the ingredients that make up the recipe name specified. It recalculates the ingredient quantities if you specify a different serving size.
- `recipes ingredient *<ingredient name>`: Functions similarly to `recipes recipe`, displays info for particular ingredient. Omitting argument prompts you for a name.
- `recipes ingredients`: Displays all of the ingredients you have saved, from here you can then view their prices -- and any other information that gets implemented.
- `recipes kitchen recipes`: Displays all possible recipes you can make from what is in your kitchen
- `recipes kitchen ingredients`: Displays all possible recipes you can make from what is in your kitchen
- `recipes errors`: Displays any problems that exist within the information you have saved -- incorrect ingredient units, missing values, etc.

Each and every one of these commands also works regardless of ordering. Query terms must however be ordered correctly and be written after any commands as above.

All of these commands just display information, but you can edit all of this information with the inclusion of the `edit` command. Using this will open up a menu to `add`, `remove` or `change` entries, or even `reset` the whole thing.

...
