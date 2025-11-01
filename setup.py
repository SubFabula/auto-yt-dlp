from setuptools import setup, find_packages

with open('README.md', 'r') as f:
  longdescription = f.read()

with open('auto_yt_dlp/__init__.py', 'r') as f:
  M__init__ = f.read()
  # __version__Index = M__init__.index('"') + 1
  # __version__EndIndex = M__init__.index('"', __version__Index)
  M__init__Split = M__init__.split()
  __version__ = M__init__Split[2].strip('"')
  print(f'----FROM `setup.py`: {__version__}----') # For the workflow console

setup(
  name='auto-yt-dlp',
  version=__version__,
  author='SubFabula',
  keywords=['gui', 'media-downloader'],
  packages=['auto_yt_dlp'],
  python_requires='==3.13',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.13',
    'Operating System :: Microsoft :: Windows',
  ],
  include_package_data=True,
  install_requires=[
    'yt-dlp',
    'pywebview',
    'qtpy',
    'PySide6>=6.9.0',
  ],
  entry_points={
    'console_scripts': [
      'autoytdlp = auto_yt_dlp.__main__:run',
      'auto-yt-dlp = auto_yt_dlp.__main__:run',
      'auto_yt_dlp = auto_yt_dlp.__main__:run',
    ],
  },
  description = '"A feature-rich command-line audio/video downloader" "...with a simple graphical interface".',
  long_description=longdescription,
  long_description_content_type='text/markdown',
  url='https://github.com/SubFabula/auto-yt-dlp',
  project_urls={
    'Source Code': 'https://github.com/SubFabula/auto-yt-dlp',
    'Bug Tracker': 'https://github.com/SubFabula/auto-yt-dlp/issues',
    'Q&A': 'https://github.com/SubFabula/auto-yt-dlp/discussions',
  },
)
