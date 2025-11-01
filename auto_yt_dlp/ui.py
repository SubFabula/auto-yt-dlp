import webview
import os
import logging
from . import config, utils
if config.QTPY == True:
  import qtpy

logger = logging.getLogger(__name__)

# Set the paths
WEB_PATH = os.path.join(config.ROOT, r'web\index.html')
logger.debug(f'WEB_PATH: {WEB_PATH}')
ICO_PATH = os.path.join(config.ROOT, r'web\favicon.ico')
logger.debug(f'ICO_PATH: {ICO_PATH}')

# Start with the app
def echo():
   logger.debug("Functions have been exposed from Python.")

def expose(window):
  window.expose(echo)  # expose a function during the runtime

def get_url(window):
  WEB_URL = str(window.get_current_url())
  logger.debug(f'WEB_URL: {WEB_URL}')
  return WEB_URL

def bulk_func(window):
  expose(window)
  get_url(window)

# Respond to events
def on_before_show(window):
  logger.debug(f'window.native: {window.native}')

def on_initiliaze(renderer):
  print("The app will stop working once it or the command prompt is closed/exited.\nTo stop all processes, press Ctrl + C.")
  logger.debug(f'GUI is initialized with the renderer {renderer}')

def on_resize(window, width, height):
  print('Please do not resize the window!')
  logger.debug('New dimensions were {width} x {height}'.format(width=width, height=height))
  window.resize(config.WIDTH, config.HEIGHT)
  logger.debug(f'Default size has been applied {config.WIDTH} x {config.HEIGHT}'.format(width=config.WIDTH, height=config.HEIGHT))

def on_close():
    print('Window is closed!')
    logger.info('Window is closed!')

# Start the app
def start():
  logger.debug("`ui.start()` has been called!")
  window = webview.create_window(
    title='Auto Youtube Audio/Video Downloader Plus',
    url=WEB_PATH,
    width=config.WIDTH,
    height=config.HEIGHT,
    x=0,
    y=0,
    resizable=False,
    fullscreen=False,
    frameless=False,
    focus=True,
    confirm_close=True,
    shadow=False,
    transparent=False,
    zoomable=False
    )

  window.events.before_show += on_before_show
  window.events.initialized += on_initiliaze
  window.events.resized += on_resize
  window.events.closed += on_close

  window.expose(utils.open_file_dialog, utils.runCMD)
  window.state.DEBUG = config.DEBUG
  window.state.LOGGING = config.LOGGING

  if config.QTPY == True:
    try: # Try Qt
      webview.start(bulk_func, {window}, ssl=False, gui="qt", icon=ICO_PATH, debug=config.DEBUG)
    except qtpy.PythonQtError or qtpy.QtBindingsNotFoundError as e:
      print(f"Qt isn't working! Switching to EdgeChromium!\n{e}")

      if e == qtpy.PythonQtError or e == qtpy.QtBindingsNotFoundError: # Switch to EdgeChromium if Qt isn't working
        try:
          webview.start(bulk_func, {window}, ssl=False, gui="edgechromium", icon=ICO_PATH, debug=config.DEBUG)
        except RuntimeError as e:
          print(f"EdgeChromium isn't working! Switching to any available viewer!\n{e}")

  if config.QTPY != True: # Use EdgeChromium if Qt doesn't exist
    try:
      webview.start(bulk_func, {window}, ssl=False, gui="edgechromium", icon=ICO_PATH, debug=config.DEBUG)
    except RuntimeError as e:
      print(f"EdgeChromium isn't working! Switching to any available viewer!\n{e}")