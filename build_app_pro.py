import PyInstaller.__main__
import shutil
import os

APP_NAME = "anyGIF Pro"
INFO_PLIST_PATH = "Info_pro.plist"  # Your custom plist file
BUILD_DIR = f"dist/{APP_NAME}.app/Contents"

PyInstaller.__main__.run([
    'main_macos_pro.py',
    '--windowed',
    '--noconsole',
    '--collect-all',
    'ffmpeg-python',
    '--add-binary=bin/ffmpeg:.',  # Include FFmpeg
    '--osx-bundle-identifier', 'com.f1dg3t.anygifpro',  # Set identifier
    '-n', APP_NAME,
    '--icon=res/appIcon.icns'
])

# **Step 2: Manually Replace Info.plist**
if os.path.exists(BUILD_DIR):
    shutil.copy(INFO_PLIST_PATH, os.path.join(BUILD_DIR, "Info_pro.plist"))
    print(f"✅ Custom Info.plist applied to {BUILD_DIR}")

print("🎉 Pro Build complete!")
