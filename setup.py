from setuptools import setup, find_packages
from auto_yt_dlp.__init__ import __version__

with open('README.md', 'r') as f:
  description = f.read()

setup(
  name='auto-yt-dlp',
  version=__version__,
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'yt-dlp',
    'pywebview',
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
