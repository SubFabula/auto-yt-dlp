import eel
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
print("ROOT: ", ROOT)
WEB_DIR = os.path.join(ROOT, "web")
print("WEB_DIR: ", WEB_DIR)

eel.init(WEB_DIR)

@eel.expose
def onLine(): # To (hopefully) let the `web` know that the `eel` process is online or not.
  return True

def start():
  try:
    print("To stop the process, (after a second or two) exit the current command panel. If the app doesn't exit automatically, please just close all visible instances of the app.")
    eel.start('index.html', host="localhost", size=(655, 680), port=0)
  except (SystemExit, KeyboardInterrupt):
    pass
