import logging
from auto_yt_dlp import __version__, config, utils

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

formatter = logging.Formatter(config.LOGGING_FORMAT)

if config.LOGGING_TO_FILE == True:
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

logger = logging.getLogger(__name__)

#__MAIN__
def run():
  from auto_yt_dlp import ui # Importing it here so that it doesn't start logging before `__main__.py` is done with the `LOGGING` part
  ui.start()

if __name__ == "__main__":
  logger.info(f"___APP IS STARTING___({__version__})")
  logger.debug(f'config.ROOT: {config.ROOT}')
  run()