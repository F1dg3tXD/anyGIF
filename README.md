# anyGIF
A UI-based program to convert any video file to a GIF using ffmpeg.

## Features
* Custom resolutions
* Custom framerate remuxing
* Renamable output

# Building
`Requires python 3.11.3`

## Windows
* Clone repo
* `pip install requirements.txt`
* `pyinstaller --onefile --windowed --icon=res/appIcon.ico --add-data "bin:bin" --collect-all ffmpeg-python -n anyGIF main.py`

   It is really that basic.

## Building Windows Installer
* Install [INNO Setup](https://jrsoftware.org/isinfo.php)
* Run Build Installer build task.

## MacOS
* Clone repo
* `pip install requirements.txt`
* `python build_app.py`

## Contributing
Any help is appreciated; UI themes and other improvements will be community-driven.

## Disclaimer
I'm not a programmer, I fr failed 2 COMPSCI classes in university. 
