import logging
import subprocess
import webview
import json
from . import __version__, config

logger = logging.getLogger(__name__)

def open_file_dialog():
  try:
    window = webview.windows[0]
  except:
    logger.error('No existing Window found!')
    return None
  output_path_list = window.create_file_dialog(webview.FileDialog.FOLDER, allow_multiple=False)
  
  if config.LOGGING_DETAIL == True:
    logger.debug(f'output_path_list: {output_path_list}')
  logger.debug(f'output_path_list[0]: {output_path_list[0]}')
  window.state.output_path = output_path_list[0]
  logger.debug(f'window.state.output_path: {window.state.output_path}')
  return window.state.output_path

def runCMD(cmd):
  window = webview.windows[0]
  logger.info(f'cmd: {cmd}')
  cmdOutput = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

  for pyLine in cmdOutput.stdout:
    if config.LOGGING_DETAIL == True:
      logger.debug(f'cmdOutput/pyLine:{pyLine}')
    jsLine = json.dumps(pyLine)
    jsLineOpen_R = jsLine.rstrip('"')
    jsLineOpen = jsLineOpen_R.lstrip('"')

    if config.LOGGING_DETAIL == True:
      logger.debug(f'cmdOutput/jsLine: {jsLine}')
      logger.debug(f'cmdOutput/jsLineOpen_R: {jsLineOpen_R}')

    logger.info(f'cmdOutput/jsLineOpen: {jsLineOpen}')
    window.evaluate_js(f'document.getElementById("command_output_text").value += `{jsLineOpen}`;'
                       'window.scrollBy(0, 10000);')
    
  logger.info('`runCMD` process has finished!')