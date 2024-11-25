import logging

FORMAT = "%(asctime)s | %(levelname)s | %(filename)s: %(funcName)s -> \"%(message)s\""

def setup_logger(name:str):
    logger = logging.getLogger(name)
    logging.basicConfig(filename='app.log', format=FORMAT, level=logging.INFO, filemode='w')
    return logger