import logging
from auto_yt_dlp import __version__, config

#LOGGING
logger = logging.getLogger()
logger.setLevel(config.LOGGING_LEVEL)
logger.propagate = False

if config.LOGGING == False:
   logger.setLevel(logging.CRITICAL + 1)

for handlers in logger.handlers[:]:
    logger.removeHandler(handlers)

logger_filehandler = logging.FileHandler(
     filename=config.LOGGING_FILE_NAME,
     mode=config.LOGGING_FILEMOD,
     encoding=config.LOGGING_ENCODING
     )

if config.LOGGING_TO_FILE == True:
  formatter = logging.Formatter(config.LOGGING_FORMAT)
  logger_filehandler.setFormatter(formatter)
  logger.addHandler(logger_filehandler)
elif config.LOGGING_TO_FILE == False:
  logger.removeHandler(logger_filehandler)

logger_consolehandler = logging.StreamHandler()

if config.LOGGING_TO_CONSOLE == True:
  logger_consolehandler.setFormatter(formatter)
  logger.addHandler(logger_consolehandler)
elif config.LOGGING_TO_CONSOLE == False:
  logger.removeHandler(logger_consolehandler)


#__MAIN__
def run():
  from auto_yt_dlp import ui # Importing it here so that it doesnt start logging before `__main__.py`
  ui.start()

if __name__ == "__main__":
  logging.info("___APP IS STARTING___")
  logging.debug(f'config.ROOT: {config.ROOT}')
  run()