import PyInstaller.__main__
import shutil
import os
import sys

APP_NAME = "anyGIF Pro"
INFO_PLIST_PATH = "Info_pro.plist"  # Your custom plist file
BUILD_DIR = f"dist/{APP_NAME}.app/Contents"


def build_macos():
    PyInstaller.__main__.run([
        'main_macos_pro.py',
        '--windowed',
        '--noconsole',
        '--collect-all', 'ffmpeg-python',
        '--add-binary=bin/ffmpeg:.',  # Include FFmpeg
        '--osx-bundle-identifier', 'com.f1dg3t.anygifpro',  # Set identifier
        '-n', APP_NAME,
        '--icon=res/appIcon.icns'
    ])

    # **Step 2: Manually Replace Info.plist**
    if os.path.exists(BUILD_DIR):
        # Copy to Info.plist so mac bundle sees it as the app Info
        shutil.copy(INFO_PLIST_PATH, os.path.join(BUILD_DIR, "Info.plist"))
        print(f"✅ Custom Info.plist applied to {BUILD_DIR}")

    print("🎉 Pro macOS Build complete!")


def build_linux():
    linux_name = APP_NAME.replace(" ", "_")

    PyInstaller.__main__.run([
        'main_pro.py',
        '--windowed',
        '--noconsole',
        '--collect-all', 'ffmpeg-python',
        '--add-binary=bin/ffmpeg:bin',  # Include FFmpeg in a bin/ folder
        '-n', linux_name,
        '--icon=res/appIcon.png'
    ])

    dist_path = f"dist/{linux_name}"

    if os.path.exists(dist_path):
        shutil.copy('res/appIcon.png', os.path.join(dist_path, 'icon.png'))

        desktop_content = f"""[Desktop Entry]
Name={APP_NAME}
Exec=./{linux_name}
Icon=icon.png
Type=Application
Terminal=false
Categories=Utility;
"""

        desktop_path = os.path.join(dist_path, f"{linux_name}.desktop")
        with open(desktop_path, 'w') as f:
            f.write(desktop_content)
        os.chmod(desktop_path, 0o755)

        print(f"✅ Desktop entry created at {desktop_path}")

    print("🎉 Pro Linux Build complete!")


if __name__ == "__main__":
    if sys.platform == 'darwin':
        build_macos()
    elif sys.platform.startswith('linux'):
        build_linux()
    else:
        print(f"Unsupported platform: {sys.platform}")
