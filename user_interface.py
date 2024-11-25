import sys
from logger_config import setup_logger
import info_commands as info
import edit_commands as edit

COMMANDS:dict = {'edit':0, 'search':1, 'recipe':2, 'recipes':3, 'ingredient':4, 'ingredients':5, 'kitchen':6, 'errors':7}
LOGGER = setup_logger(__name__)

def info_router(remaining_ids:str, queries:list) -> None:
    if remaining_ids:
        id = remaining_ids[0]
    match id:
        case '2':
            info.recipe(remaining_ids, queries)
        case '3':
            info.recipes(remaining_ids, queries)
        case '4':
            info.ingredient(remaining_ids, queries)
        case '5':
            info.ingredients(remaining_ids, queries)
        case '6':
            info.kitchen(remaining_ids, queries)
        case '7':
            info.errors(remaining_ids, queries)

def edit_router(remaining_ids:str, queries:list) -> None:
    id = remaining_ids[0]
    match id:
        case '2':
            edit.recipe(remaining_ids, queries)
        case '3':
            edit.recipes(remaining_ids, queries)
        case '4':
            edit.ingredient(remaining_ids, queries)
        case '5':
            edit.ingredients(remaining_ids, queries)
        case '6':
            edit.kitchen(remaining_ids, queries)
        case '7':
            edit.errors(remaining_ids, queries)

def search_router(remaining_ids:str, queries:list) -> None:
    id = remaining_ids[0]
    match id:
        case '2':
            LOGGER.critical("SEARCH CASE 'recipe': Not completed yet")
        case '3':
            LOGGER.error('User did "search recipes", don\'t know what to do about that.')


def validate_and_route_command_ids(command_ids:list, queries:list):
    """ Does first pass of checks on the command_ids, ensuring some validity, and then calls relevant functions based on inputs """
    if ('0' not in command_ids) and ('1' not in command_ids):
        # Do info stuff
        LOGGER.info("SUCCESS: Routing to 'info' section")
        remaining_command_ids = command_ids
        if remaining_command_ids:
            LOGGER.info(f"Calling info_router with remaining_ids = '{remaining_command_ids}'")
            info_router(remaining_command_ids, queries)
        else:
            # Don't think this can actually be triggered, other functions handle that
            LOGGER.critical("Something that doesn't make any sense to me has happened")
            print("ERROR: Command required")
        ...
    elif ('0' in command_ids) and ('1' not in command_ids):
        # Do editing stuff
        LOGGER.info("SUCCESS: Routing to 'edit' section")
        remaining_command_ids = command_ids[1:]
        if remaining_command_ids:
            LOGGER.info(f"Calling edit_router with remaining_ids = '{remaining_command_ids}'")
            edit_router(remaining_command_ids, queries)
        else:
            LOGGER.error(f"MISSING NOUN: 'edit' isn't operating on another command")
            print("ERROR: 'edit' requires another command to operate on (e.g. `edit kitchen`)")
        ...
    elif ('0' not in command_ids) and ('1' in command_ids):
        # Do search stuff
        LOGGER.info("SUCCESS: Routing to 'search' section")
        remaining_command_ids = command_ids[1:]
        if remaining_command_ids:
            LOGGER.info(f"Calling search_router with remaining_ids = '{remaining_command_ids}'")
            search_router(remaining_command_ids, queries)
        else:
            LOGGER.error(f"MISSING NOUN: 'search' isn't operating on another command")
            print("ERROR: 'search' requires command to operate on (e.g. `search recipes`)")
        ...
    else:
        # Both 'edit' and 'search' have been entered
        LOGGER.error("ERROR: Both 'edit' and 'search' have been entered")


def get_ids_from_commands(user_commands:list) -> str:
    LOGGER.info("Beginning conversion of commands to IDs")
    arg_contents:str = ""
    for key, value in COMMANDS.items():
        if key in user_commands:
            arg_contents += str(value)
    LOGGER.info(f"OUTPUT: Command IDs string is '{arg_contents}'")
    return arg_contents


def args_parser(args:list) -> tuple:
    """ Checks that arguments follow ['command', 'command, ..., 'search term', 'search term'] format,
         returns ([`commands`],[`search terms`]) if valid, else returns (None, None) """

    # Check all commands are valid
    # Must take in at least one command
    # Disallow duplicate commands
    # Only allow for invalid arguments (what will be 'search terms') *after* all of the valid arguments

    invalid_args_log = list()
    valid_args_log = list()

    valid = True
    for arg in args:
        LOGGER.info(f"------------ Checking '{arg}' ------------")
        if arg in COMMANDS:
            # Have to make sure that the command isn't after a potential search term 
            LOGGER.info(f"Is Command: '{arg}' *is* a command")
            if invalid_args_log:
                LOGGER.error(f"Invalid Position: '{arg}' has been entered after non-command term(s)")
                print(f"ERROR: '{arg}' command has been entered after non-command terms")
                valid = False
                break
            else:
                # Now have to make sure that the command isn't a duplicate
                if arg in valid_args_log:
                    LOGGER.error(f"Duplicate: '{arg}' was repeated")
                    print(f"ERROR: '{arg}' command is a duplicate ")
                    valid = False
                    break
                else:
                    LOGGER.info(f"Tests passed: '{arg}' is a valid additional argument")
            LOGGER.info(f"Logging: Adding '{arg}' to valid_args_log")
            valid_args_log.append(arg)
        else:
            LOGGER.info(f"Not a Command: Adding '{arg}' to invalid_args_log")
            invalid_args_log.append(arg)

    if not valid_args_log:
        LOGGER.info("Valid arguments were empty, so commands aren't valid")
        print("ERROR: No valid commands were entered, type `recipes help` if you need any guidance")
        valid = False

    if valid:
        LOGGER.info("Overall arguments were valid, returning appropriate output")
        return valid_args_log, invalid_args_log
    else:
        LOGGER.info("Arguments were empty or invalid, returning (None, None)")
        return None, None


if __name__ == "__main__":
    args = sys.argv[1:]
    commands, queries = args_parser(args)
    if commands:
        command_ids = get_ids_from_commands(commands)
        validate_and_route_command_ids(command_ids)

    # print(command_and_query_parser(args))

# Parse args into valid commands and queries
# For valid args, just let the routers direct it to the right place
# For invalid args, print appropriate messages 
#   Do I want to collect and communicate ALL errors? Or just the first one it catches?



# ['edit':0, 'search':1, 'recipe':2, 'recipes':3, 'ingredient':4, 'ingredients':5, 'kitchen':6, 'errors':7]
# 2 <recipe name>                           :   Shows specific recipe info
# 3                                         :   Shows all recipes
# 4 <ingredient name>                       :   Shows specific ingredient info
# 5                                         :   Shows all ingredients
# 6                                         :   Shows contents of kitchen
# 7                                         :   Shows all existing errors in the info
# 02 <recipe name>                          :   Opens editing for specific recipe
# 03                                        :   Opens editing for all recipes
# 04 <ingredient name>                      :   Opens editing for specific ingredient
# 05                                        :   Opens editing for all ingredients
# 06                                        :   Opens editing for kitchen
# 07                                        :   Opens editing for errors
# 12 <key terms>+                           :   Searches for key terms (maybe allows for 'name:recipe name', or 'time:dinner')
# 13 <key terms>+                           :   ^ Maybe just does the same as above
# 14 <key terms>+                           :   Searches for ingredients using key terms
# 15 <key terms>+                           :   ^ Maybe just does the same as above
# 16 <key terms>+                           :   Searches kitchen info for key terms
# 17 <key terms>+                           :   Searches errors -- kinda unnecessary though I feel