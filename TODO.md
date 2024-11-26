# TODO
## In progress
- Remove all 'destination command' arguments for any residual commands in `\w+_commands.py` files -- residual commands should have already been accounted for by here.
- Move all references to destination commands like `edit_kitchen` from `user_interface.py` to a separate `\w+_commands.py` file.
- Correct and remove any reference to `recipes recipe` accepting 'servings' arguments, reserve that functionality for `recipes recipe ingredients` 
- Try to create some kind of abstraction for handling inputs in the `\w+_commands.py` files, be it from `input()` or queries -- i.e. see if you can justify something
- Organise the files better because it's an absolute state -- maybe separate the JSON related stuff first
- Get `recipes recipes` -> `n` actually working like how `recipes recipe <name>` works
## Done
- Abstracted the gaudy and repetitious `validate_and_route_commands` function.
- Switch `match case` to something that checks inside
- Fix `request_recipe_name` and `get_recipe_name` functions, i.e. replace `for key in recipes` with `try: recipes[query] ...`
- Get `recipes recipe *<recipe name>` working
- Remove references to `remaining_commands` in the info file
- Probably figure out a more streamlined way of handling command combinations
## Dropped
- Implement the servings functionality for `recipes recipe \<recipe name\> \<servings\>
    Avoiding servings functionality for `recipes recipe`, reserving it instead for `recipes recipe ingredients`
- Figure out better names for these damn functions
    Too vague an objective, need to be more specific

<br>
<br>
<br>

# Discussion
- I'm trying to figure out how to format and store the cupboard.json information. I think I want Enums for the ingredients, so that you essentially can't type in a new ingredient unless it's formally added into the mix.
- I'm also struggling with how I might handle variants, for example "cherry tomatoes", "beef tomatoes", "vine tomatoes" im sandwiches, etc. Should my recipes specify every single possible variant that could be substituted, or do I store that kind of information externally? I could even try to automatically change cases with hyperspecific ingredient references to more diverse ones -- e.g. If it detects 'fish', it automatically asks what I meant more specifically, but now we're talking about introducing *categories* of foods that might be substitutable ("eggs" -> "large eggs | medium eggs"; "fish" -> "haddock | sea bass | cod | tuna steak |"). I'd need like a hierarchy of foods labels. At the very least, if I just documented common ambiguities and tried to 
