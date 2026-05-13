import os

#? You can edit some parts of the config file if you
#? need to and only if you know what you are doing.
#?
#? Please don't touch the ones that are marked with "!"
#? on either side to avoid any future problems. 
#? 
#? You can still change some ones with "!" IF you have to.
#?

#DEBUG#
DEBUG=True
LOGGING=True
LOGGING_DETAIL=False

LOGGING_TO_CONSOLE=False
LOGGING_TO_FILE=True

#!ROOT!#
ROOT = os.path.dirname(os.path.abspath(__file__))

#!LOGGING OPTIONS!#
LOGGING_FILE_NAME = os.path.join(ROOT, r'auto_yt_dlp.log')
LOGGING_ENCODING='utf-8'
LOGGING_LEVEL='DEBUG'
LOGGING_FILEMOD='a'
LOGGING_FORMAT='%(asctime)s [%(levelname)s] [%(name)s/%(module)s.py: %(lineno)d.%(funcName)s()] | %(message)s'

#!UI OPTIONS!#
QTPY=False # Automatically set to `True` at runtime if it exist
WIDTH=650
HEIGHT=670

#!OTHER LOGIC STUFF!# 
if LOGGING == True and LOGGING_TO_CONSOLE == False and LOGGING_TO_FILE == False:
  print("`LOGGING` is ACTIVE!\nBut `LOGGING_TO_CONSOLE` and `LOGGING_TO_FILE` is NOT ACTIVE!")

if LOGGING == False:
  LOGGING_TO_CONSOLE=False
  LOGGING_TO_FILE=False
elif LOGGING_TO_CONSOLE == False and LOGGING_TO_FILE == False:
  LOGGING=False

if LOGGING_TO_CONSOLE == True:
  print("`LOGGING_TO_CONSOLE` is ACTIVE!")
if LOGGING_TO_FILE == True:
  print("`LOGGING_TO_FILE` is ACTIVE!")
