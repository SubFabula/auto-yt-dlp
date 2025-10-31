import logging
import importlib
import shutil
import subprocess
from . import __version__, config

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
  try: # Check the requirements
    import webview, yt_dlp
  except ModuleNotFoundError as e:
    print(f"Please install missing modules from the following; PyWebView and Yt-Dlp modules for this app to work\n\nDo this in the console for whichever module is missing:\npython -m pip install pywebview\npython -m pip install yt-dlp\n")
    raise e

  if importlib.util.find_spec('qtpy'):
    config.QTPY = True
    try: # Check PySide6
      from PySide6 import __version__ as PySide6__version__
    except ModuleNotFoundError as e:
      print(f'Please install the missing module from the following for the app to work as indented; PySide6\n\nDo this in the console for the missing module:\npython -m pip install "PySide>=6.9.0"\n{e}')
  
  try:
    PySide6__version__
  except UnboundLocalError:
    PySide6__version__ = None
    pass

  if PySide6__version__ != None:
    if PySide6__version__ == "6.8.0": # Check PySide6 Version
      print(f'Please install the right version of the following module for the app to work as indented; PySide6>6.8.0\n\nDo this in the console to upgrade module:\npython -m pip install --upgrade "PySide>6.8.0"\n')
      assert PySide6__version__ == "6.8.0"

  if shutil.which("ffmpeg"):
    pass
  else:
    print("`ffmpeg` wasn't found! Automatically installing `ffmpeg`!")
    subprocess.run("winget install ffmpeg")

  from . import ui # Importing it here so that it doesn't start logging before `__main__.py` is done with the `LOGGING` part
  ui.start()

if __name__ == "__main__":
  logger.info(f"___APP IS STARTING___({__version__})")
  logger.debug(f'config.ROOT: {config.ROOT}')
  run()