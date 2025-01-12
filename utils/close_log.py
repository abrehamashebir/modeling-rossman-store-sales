
import logging
def close_loggers():
            """Closes all the open logging handlers."""
            for logger_name, logger in logging.Logger.manager.loggerDict.items(): # get all registered loggers
                if isinstance(logger, logging.Logger): # only use the ones that are loggers
                    for handler in logger.handlers:
                        handler.close()  # Close any file handlers.
                        logger.removeHandler(handler) # remove the handler from the logger
                        