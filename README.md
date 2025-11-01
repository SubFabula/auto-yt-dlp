<h1 align="center">Auto Youtube Audio/Video Downloader Plus</h1>
<p align="center"><em>"A feature-rich command-line audio/video downloader" "...with a simple graphical interface".</em></p>

<p align="center">
    <img src="https://raw.githubusercontent.com/SubFabula/auto-yt-dlp/main/applook.png" alt="Base Look" height="500px">
</p>

<p align="center">
    <a href="https://pypi.org/project/auto-yt-dlp/"><img src="https://img.shields.io/pypi/v/auto-yt-dlp.svg" alt="PyPI Version"></a>
    <a href="https://pypi.org/project/auto-yt-dlp/"><img src="https://img.shields.io/pypi/pyversions/auto-yt-dlp.svg" alt="PyPI Supported Versions"></a>
    <a href="https://pypi.org/project/auto-yt-dlp/"><img src="https://img.shields.io/pypi/l/auto-yt-dlp.svg" alt="License"></a>
    <a href="https://pepy.tech/project/auto-yt-dlp"><img src="https://static.pepy.tech/badge/auto-yt-dlp/month" alt="Downloads Per Month"></a>
    <a href="https://pyinstaller.readthedocs.io/en/stable/requirements.html"><img src="https://img.shields.io/badge/platform-windows-lightgrey" alt="Supported Platforms"></a>
</p>

# Showcase
<p align="center">
    <img src="https://raw.githubusercontent.com/SubFabula/auto-yt-dlp/main/appshowcase.gif" alt="Simple Showcase" height="500px">
</p>

# Content
- [How to Install & Use](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#how-to-install--use)
- [Can i contribute to this?](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#can-i-contribute-to-this)
- [Report an Issue!](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#report-an-issue)
  - [Before Reporting...](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#before-reporting)
- [Other Q&As](https://github.com/SubFabula/auto-yt-dlp/discussions/new/choose)

## How to Install & Use
### [1. PyPi Installation](https://pypi.org/project/auto-yt-dlp)
#### Requirements
- [`Python 3.10`](https://www.python.org/downloads) or higher

#### Installation & Usage
Run these commands in the command prompt/terminal:

1. Run `python -m pip install auto-yt-dlp` to install.
2. Run `python -m auto_yt_dlp` or just `auto-yt-dlp`/`auto_yt_dlp` to start the app

### 2. Download the `.exe`
> [!NOTE]
> This is work in progress.
#### Requirements
- A working computer ¯\\_\(ツ)\_/¯

#### Installation & Usage
You can head to the [releases](https://github.com/SubFabula/auto-yt-dlp/releases/latest) section and download the standalone version of the app!

Just put the `.exe` file wherever and double click on it to start it.

### 3. Github Download
#### Requirements
- [`Python 3.10`](https://www.python.org/downloads) or higher

#### Installation & Usage
Follow these steps to download and use the app.

1. Clone/download the repository.
2. Open command prompt/terminal and `cd` into the project's root folder.
3. Run `python -m pip install -r requirements.txt`
4. Run `python -m auto_yt_dlp` to run the application

## Can i contribute to this?
Yes, you can. (And also thanks, i really appreciate it :D)

How?

In whatever you think you can by adding any missing features (by [forking](https://github.com/SubFabula/auto-yt-dlp/fork) it), telling me any mistakes/errors an whatnot from the [issues](https://github.com/SubFabula/auto-yt-dlp/issues/new) (check the ["Report an Issue!"](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#report-an-issue) title first!) or localizing it to your native language or to the ones you know (just make a fork and translate it. I will do the in-app language settings stuff later.)

## Report an Issue!
> [!NOTE]
> Logging is on by default. So, once you run the app, there will be an `auto_yt_dlp.log` file created in the app folder. If you have any errors or problems, provide the log file as well. Some errors might not have been saved to the log file, make sure to check the console and copy the errors from there too. <br>
> But, if you want to disable this, just go to the `config.py` file in the app folder. Open it, find `LOGGING` and change the `True` to `False`.

You can report any problems from right __[here](https://github.com/SubFabula/auto-yt-dlp/issues/new)__.

### Before Reporting...
> [!NOTE]
> If you get any errors in the Command Output in the app, it's probably something to do with [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) or the way you wrote your `URL` or `Output Path`.

> [!IMPORTANT]
> If you are manually setting your path, don't forget to write the file name and extension at the end of the folder directory. <br>
> Example: `C:\Users\[USERNAME]\Desktop\[FILE_NAME].[FILE_EXTENSION]`<br>
> Another example: `C:\Users\myPC\Desktop\FunnyVideo.mp4`<br>
> <br>
> If you want to keep the audio/video's title and extention, just set the `Output Path` by browsing (the `Browse` button) or, you can just put `%(title)s.%(ext)s` where you would put your file name and extension.<br>
> <br>
> The app will automatically turn any `/` into `\` for the Output Directory since [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) doesn't accept `Output Path`s with`/`.

# TODO
- [x] Make the app launch-able from CMD.
- [x] Make the app and CMD exit together.
- [x] Design the UI in a re-usable way.
- [x] Make the app input CMD codes and run it.
- [x] Upload to PyPi for others to be able to access it easily.
- [ ] Add every other option of [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).
