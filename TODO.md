# TODO
## In progress
- Probably clean up the imports in the `commands/` files, and maybe elsewhere, with all this file system changing it'll probs be a mess.
- Implement `add`, `remove` functionality for `edit recipes`
- Implement `edit` functionality for `recipes recipes` so that I finally don't have to edit the json directly. 
- Organise the files better because it's an absolute state -- maybe separate the JSON related stuff first
- Get `recipes recipes` -> `n` actually working like how `recipes recipe <name>` works
## Done
- Try to create some kind of abstraction for handling inputs in the `commands/` files, be it from `input()` or queries -- i.e. see if you can justify something <- Made some solid progress with this already, so that's great actually.
- Make `elif`s more efficient with command branching -- I think I'll have to convert the `commands` to something hashable (and sets/lists aren't), so maybe command IDs are coming back.
- Potentially separate the routing from the 'general' command functions
- Rework the whole routing procedure to work with the new `commands` folder
- Potentially group together all commands in a `commands` folder and organise by 'verb' rather than 'noun' -- as they are atm -- since similar 'verb's seem to share a lot of code

## Dropped


<br>
<br>
<br>

# Discussion
- I'm trying to figure out how to format and store the cupboard.json information. I think I want Enums for the ingredients, so that you essentially can't type in a new ingredient unless it's formally added into the mix.
- I'm also struggling with how I might handle variants, for example "cherry tomatoes", "beef tomatoes", "vine tomatoes" im sandwiches, etc. Should my recipes specify every single possible variant that could be substituted, or do I store that kind of information externally? I could even try to automatically change cases with hyperspecific ingredient references to more diverse ones -- e.g. If it detects 'fish', it automatically asks what I meant more specifically, but now we're talking about introducing *categories* of foods that might be substitutable ("eggs" -> "large eggs | medium eggs"; "fish" -> "haddock | sea bass | cod | tuna steak |"). I'd need like a hierarchy of foods labels. At the very least, if I just documented common ambiguities and tried to 
