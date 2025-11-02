import pyinstaller_versionfile
import re

with open('auto_yt_dlp/__init__.py', 'r') as f:
  __init__ = f.read()
  __init__ = __init__.split()
  __version__ = __init__[2].strip('"')
  print(f'----FROM `file_version_MK`: __version__ = {__version__}----')
  match_th = re.search(r"[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+|.(post|rc|b|a|dev)[0-9]+)?$", __version__)
  print(f'----FROM `file_version_MK`: match_th = {match_th}----')
  match_rd = re.search(r"[0-9]+\.[0-9]+\.[0-9]", match_th.group(0))
  print(f'----FROM `file_version_MK`: match_rd = {match_rd}----')
  if match_th.group(0) == match_rd.group(0):
    __version__ = match_rd.group(0)
    print(f'----FROM `file_version_MK`: __version__ = {__version__}----')
  else:
    match_th = match_th.group(0).split(".")
    print(f'----FROM `file_version_MK`: match_th = {match_th}----')
    match_th_3 = re.search(r"[0-9]+", match_th[3])
    print(f'----FROM `file_version_MK`: match_th_3 = {match_th_3}----')
    match_th = f"{match_th[0]}.{match_th[1]}.{match_th[2]}.10{match_th_3[0]}"
    print(f'----FROM `file_version_MK`: match_th = {match_th}----')
    __version__ = match_th
    print(f'----FROM `file_version_MK`: __version__ = {__version__}----')

pyinstaller_versionfile.create_versionfile(
  output_file='versionfile.txt',
  version=__version__,
  company_name='SubFabula',
  file_description='"A feature-rich command-line audio/video downloader" "...with a simple graphical interface"',
  internal_name='Auto Youtube Audio/Video Downloader Plus',
  legal_copyright='Created by SubFabula © 2025. License: Unlicense.',
  original_filename='auto_yt_dlp',
  product_name='auto_yt_dlp.exe',
  translations=["0x0409", "0x0809"] # [0x0409 U.S. English], [0x0809 U.K. English]
)

print(f'----FROM `file_version_MK`: DONE!!!----')