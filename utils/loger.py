import logging
def logger(name):
    """Sets up a logger instance with the given name."""
    logger = logging.getLogger(name) # get a logger with the given name
    # set the logging settings only once, if no handlers exist for this logger
    if not logger.hasHandlers():
      logging.basicConfig(
        level=logging.INFO,  # Minimum level of messages to log
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', # log message format
        handlers=[
            logging.FileHandler("experiment.log"), # save to logfile
            logging.StreamHandler() # print to console
        ]
    )
    return logger