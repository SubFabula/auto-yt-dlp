from setuptools import setup, find_packages

with open('README.md', 'r') as f:
  description = f.read()

with open('auto_yt_dlp/__init__.py', 'r') as f:
  M__init__ = f.read()
  # __version__Index = M__init__.index('"') + 1
  # __version__EndIndex = M__init__.index('"', __version__Index)
  M__init__Split = M__init__.split()
  __version__ = M__init__Split[2].strip('"')
  print(f'----FROM `setup.py`: {__version__}----')

setup(
  name='auto-yt-dlp',
  version=__version__,
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'yt-dlp',
    'pywebview',
    'pythonnet>=3.0.0'
  ],
  entry_points={
    'console_scripts': [
      'auto-yt-dlp = auto_yt_dlp:run',
      'auto_yt_dlp = auto_yt_dlp:run',
    ],
  },
  long_description=description,
  long_description_content_type='text/markdown',
)
