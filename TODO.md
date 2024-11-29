# TODO
## In progress
- Just used `recipes recipe` and expected a numbered list but obvs I implemented a manual text input -- not sure I should keep that now.
- When prompted for manual input for 'recipes', don't just offer numerical input but also recipe name input.
- Probably clean up the imports in the `commands/` files, and maybe elsewhere, with all this file system changing it'll probs be a mess.
- Implement `add`, `remove` functionality for `edit recipes`
- Implement `edit` functionality for `recipes recipes` so that I finally don't have to edit the json directly. 
- Organise the files better because it's an absolute state -- maybe separate the JSON related stuff first
- Get `recipes recipes` -> `n` actually working like how `recipes recipe <name>` works
## Done
- Update the default 'add recipe' format to the actual `meta, ingredients : primary, required, ...` format
- When creating a new recipe, run a check to make sure that the name doesn't already exist, and if it does suggest 'changing' or 'resetting' instead

## Dropped


<br>
<br>
<br>

# Discussion
- I'm trying to figure out how to format and store the cupboard.json information. I think I want Enums for the ingredients, so that you essentially can't type in a new ingredient unless it's formally added into the mix.
- I'm also struggling with how I might handle variants, for example "cherry tomatoes", "beef tomatoes", "vine tomatoes" im sandwiches, etc. Should my recipes specify every single possible variant that could be substituted, or do I store that kind of information externally? I could even try to automatically change cases with hyperspecific ingredient references to more diverse ones -- e.g. If it detects 'fish', it automatically asks what I meant more specifically, but now we're talking about introducing *categories* of foods that might be substitutable ("eggs" -> "large eggs | medium eggs"; "fish" -> "haddock | sea bass | cod | tuna steak |"). I'd need like a hierarchy of foods labels. At the very least, if I just documented common ambiguities and tried to 
