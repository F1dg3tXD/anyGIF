[Setup]
; Basic information about the installer
AppName=anyGIF
AppVersion=0.0.2a
DefaultDirName={pf}\anyGIF
DefaultGroupName=anyGIF
OutputBaseFilename=anyGIF_0_0_2a
Compression=lzma
SolidCompression=yes

[Files]
; The main executable
Source: "dist\anyGIF.exe"; DestDir: "{app}"; Flags: ignoreversion
; Any additional files or folders to include
Source: "dist\bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs
Source: "dist\res\*"; DestDir: "{app}\res"; Flags: ignoreversion recursesubdirs

[Icons]
; Add an icon on the desktop
Name: "{commondesktop}\anyGIF"; Filename: "{app}\anyGIF.exe"
; Add an icon in the Start menu
Name: "{group}\anyGIF"; Filename: "{app}\anyGIF.exe"

[Run]
; Optionally run the app after installation
Filename: "{app}\anyGIF.exe"; Description: "Launch anyGIF"; Flags: nowait postinstall skipifsilent
