# Plan:
- HARD: Be able to type in the ingredients that you have, and then find recipes that are closest to that/what you can already make
- MEDIUM: Be able to find recipes that require the minimum ingredients to buy/that is the lowest cost for you to buy -- requires a `cupboards.json`
- EASY: Be able to specify meal types that you're looking for: 'breakfast, lunch, dinner, snack'
- WIP: Create a system for streamlining the addition of new recipes
- EASY: Be able to calculate prices of specific recipes
- Be able to flag potential ingredient duplicates (e.g. 'basil'/'basil leaves', 'mushrooms'/'chestnut mushrooms', 'miso soup mix'/'miso soup')
- Fix the discrepancies between ingredients and what is bought (e.g. 'loaf' -> #? 'bread slice', 'garlic' -> #? 'garlic clove') 
- Incorporate serving, and potentially ultimately calorie information

## `Recipes.json`
```json
{
    "example recipe name" : {
        "meta" : {
            "url" : "www.this.is/just/an/example/?q=url",
            "time" : "dinner | lunch | breakfast | snack",
            "servings": "n",
            "keywords" : "one keyword | another keyword"
        },
        "primary" : {
            `ingredient` : `quantity`,
            `ingredient` : `quantity`
        },
        "secondary" : {
            "required" : {
                `ingredient` : `quantity`
            },
            "optional" : {
                `ingredient` : `quantity`
            }
        }
    }
}
```

## Discussion
- I'm trying to figure out how to format and store the cupboard.json information. I think I want Enums for the ingredients, so that you essentially can't type in a new ingredient unless it's formally added into the mix.
- I'm also struggling with how I might handle variants, for example "cherry tomatoes", "beef tomatoes", "vine tomatoes" im sandwiches, etc. Should my recipes specify every single possible variant that could be substituted, or do I store that kind of information externally? I could even try to automatically change cases with hyperspecific ingredient references to more diverse ones -- e.g. If it detects 'fish', it automatically asks what I meant more specifically, but now we're talking about introducing *categories* of foods that might be substitutable ("eggs" -> "large eggs | medium eggs"; "fish" -> "haddock | sea bass | cod | tuna steak |"). I'd need like a hierarchy of foods labels. At the very least, if I just documented common ambiguities and tried to 
