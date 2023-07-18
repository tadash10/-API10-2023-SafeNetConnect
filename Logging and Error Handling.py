import logging

def setup_logging():
    logging.basicConfig(filename='api_script.log', level=logging.INFO)

def log_error(exception):
    logging.error(str(exception))
