from logger_config import setup_logger
from user_interface import *


def main():
    args = sys.argv[1:]
    commands, queries = args_parser(args)
    LOGGER.info(f'Commands: {commands}, Queries: {queries}')
    if commands:
        command_ids = get_ids_from_commands(commands)
        LOGGER.info(f"Command IDs: '{command_ids}'")
        validate_and_route_command_ids(command_ids, queries)
    else:
        LOGGER.error(f"Entered commands are invalid")

if __name__ == "__main__":
    logger = setup_logger(__name__)
    main()
    