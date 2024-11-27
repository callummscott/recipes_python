from logger_config import setup_logger
from router import *


def main():
    args = sys.argv[1:]
    commands, queries = args_parser(args)
    LOGGER.info(f'Commands: {commands}, Queries: {queries}')
    if commands:
        validate_and_route_commands(commands, queries)
    else:
        LOGGER.error(f"Entered commands are invalid")

if __name__ == "__main__":
    logger = setup_logger(__name__)
    main()
    