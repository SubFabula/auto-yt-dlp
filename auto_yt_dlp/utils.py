import logging
import subprocess
import webview
import json
import os
import signal
import pathlib
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
  try:
    window = webview.windows[0]
  except:
    logger.error('No existing Window found!')
    return None
  window.state.kill_runCMD = False
  logger.info(f'cmd: {cmd}')
  subprocess.Popen('echo To stop the download process, press "Ctrl + C" in the terminal.', shell=True)
  downloadProcess = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
  window.state.runCMD_isRunning = True

  for pyLine in downloadProcess.stdout:
    if window.state.kill_runCMD == True:
      downloadProcess.send_signal(signal.SIGINT) 
      os.kill(downloadProcess.pid, signal.SIGTERM)
    if config.LOGGING_DETAIL == True:
      logger.debug(f'downloadProcess/pyLine:{pyLine}')
    jsLine = json.dumps(pyLine)
    jsLineOpen_R = jsLine.rstrip('"')
    jsLineOpen = jsLineOpen_R.lstrip('"')

    if config.LOGGING_DETAIL == True:
      logger.debug(f'downloadProcess/jsLine: {jsLine}')
      logger.debug(f'downloadProcess/jsLineOpen_R: {jsLineOpen_R}')

    logger.info(f'downloadProcess/jsLineOpen: {jsLineOpen}')
    window.evaluate_js(f'document.getElementById("command_output_text").value += `{jsLineOpen}`;'
                       'window.scrollBy(0, 10000);')
    

    #jsLO_download_rfind = jsLineOpen.rfind('[download]')
    #jsLO_download_rfind = jsLineOpen.rfind('[download]')

    #jsLO_Merger_rfind = jsLineOpen.rfind('[Merger]')
    #jsLO_MergerExtensionStart_rfind = jsLineOpen.rfind('.', jsLO_Merger_rfind)
    #jsLO_MergerExtensionEnd_find = jsLineOpen.find('\\', jsLO_MergerExtensionStart_rfind)
    #jsLineOpen.

    #jsLO_MergerPathStart_rindex = jsLineOpen.rindex('"', jsLO_Merger_rfind) forgot what i was doing for a sec
    #jsLO_MergerPathEnd_index = jsLineOpen.index('"', jsLO_Merger_rfind)
  
  subprocess.Popen('echo Download process has ended!', shell=True)
  logger.info('`runCMD` process has finished!')
  window.state.runCMD_isRunning = False

def openDownload_sDirect(path):
  try:
    window = webview.windows[0]
  except:
    logger.error('No existing Window found!')
    return None

  logger.debug(f'path: {path}')
  
  if window.state.isItFolder:
    subprocess.run(f'explorer "{os.path.expandvars(rf'{path}')}"')
  else:
    subprocess.run(f'explorer /select,"{os.path.expandvars(rf'{path}')}"')