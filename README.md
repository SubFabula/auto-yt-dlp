![applook](https://raw.githubusercontent.com/SubFabula/auto-yt-dlp/refs/heads/main/applook.png)

"A feature-rich command-line audio/video downloader" "...with a simple graphical interface".

# Content
- [Can i contribute to this?](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#can-i-contribute-to-this)
- [Report an Issue!](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#report-an-issue)
  - [Before Reporting...](https://github.com/SubFabula/auto-yt-dlp?tab=readme-ov-file#before-reporting)
- [Other Q&As](https://github.com/SubFabula/auto-yt-dlp/discussions/new/choose)

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
