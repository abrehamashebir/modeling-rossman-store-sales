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
            logging.FileHandler("../data/experiment.log"), # save to logfile
            logging.StreamHandler() # print to console
        ]
    )
    return logger

# def close_loggers():
#             """Closes all the open logging handlers."""
#             for logger_name, logger in logging.Logger.manager.loggerDict.items(): # get all registered loggers
#                 if isinstance(logger, logging.Logger): # only use the ones that are loggers
#                     for handler in logger.handlers:
#                         handler.close()  # Close any file handlers.
#                         logger.removeHandler(handler) # remove the handler from the logger
                        