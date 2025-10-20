import webview
import os
import logging
from auto_yt_dlp import config

logger = logging.getLogger(__name__)

# Set the paths
WEB_PATH = os.path.join(config.ROOT, r'web\index.html')
logging.debug(f'WEB_PATH: {WEB_PATH}')
ICO_PATH = os.path.join(config.ROOT, r'web\favicon.ico')
logging.debug(f'ICO_PATH: {ICO_PATH}')

#js-api
class API():
  pass

def open_file_dialog_Py():
  try:
    window = webview.windows[0]
  except:
    logging.error('No existing Window found!')
    return None
  output_path_list = window.create_file_dialog(webview.FileDialog.FOLDER, allow_multiple=False)
  logger.debug(f'output_path_list: {output_path_list}')
  logger.debug(f'output_path_list[0]: {output_path_list[0]}')
  window.state.output_path = output_path_list[0]
  logger.debug(f'window.state.output_path: {window.state.output_path}')
  return window.state.output_path

# Start with the app
def echo():
   logger.debug("Functions have been exposed from Python.")

def expose(window):
    window.expose(echo)  # expose a function during the runtime
  
def get_url(window):
  WEB_URL = str(window.get_current_url())
  logging.debug(f'WEB_URL: {WEB_URL}')
  return WEB_URL

def bulk_func(window):
  expose(window)
  WEB_URL = get_url(window)
  window.state.pyWINDOW = {'title': window.title, 'url': WEB_URL}
  
# Respond to events
def on_before_show(window):
  logging.debug(f'window.native: {window.native}')

def on_initiliaze(window, renderer):
  print("The app will stop working once it or the command prompt is closed/exited.")
  logging.debug(f'GUI is initialized with the renderer {renderer}')

def on_resize(window, width, height):
  print('Please do not resize the window!')
  logging.debug('New dimensions were {width} x {height}'.format(width=width, height=height))
  window.resize(config.WIDTH, config.HEIGHT)
  logging.debug(f'Default size has been applied {config.WIDTH} x {config.HEIGHT}'.format(width=config.WIDTH, height=config.HEIGHT))

def on_close():
    logging.info('Window is closed!\n')

# Start the app
def start():
  logging.debug("`ui.start()` has been called!")
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

  window.expose(open_file_dialog_Py)
  window.state.DEBUG = config.DEBUG
  window.state.LOGGING = config.LOGGING

  webview.start(bulk_func, window, ssl=False, gui="qt", icon=ICO_PATH, debug=config.DEBUG)
  