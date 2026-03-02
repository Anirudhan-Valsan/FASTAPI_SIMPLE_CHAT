import logging

def setup_logger():
    # date time / info / message
    logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")


    return logging.getLogger("llm_app")


logger = setup_logger()