# https://pyinstaller.org/en/stable/usage.html

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main_macos.py',
    '--windowed',
    '--noconsole',
    '--collect-all',
    'ffmpeg-python',
    '--add-binary=bin/ffmpeg:.',  # Include FFmpeg in the bundle
    '-n', 'anyGIF',
    '--icon=appIcon.icns'
])
