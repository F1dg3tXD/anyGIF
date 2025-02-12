[Setup]
AppName=anyGIF Pro
AppVersion=0.0.4a
DefaultDirName={pf}\anyGIF
DefaultGroupName=anyGIF
OutputDir=.
OutputBaseFilename=anyGIF_Pro_0_0_4a
Compression=lzma
SolidCompression=yes
SetupIconFile=res\winIcon.ico

[Files]
Source: "bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs
Source: "dist\anyGIF_Pro.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "res\appIcon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "redist\VC_redist.x64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Icons]
Name: "{commondesktop}\anyGIF"; Filename: "{app}\anyGIF_Pro.exe"; WorkingDir: "{app}"
Name: "{userprograms}\anyGIF"; Filename: "{app}\anyGIF_Pro.exe"; WorkingDir: "{app}"

[Run]
Filename: "{tmp}\VC_redist.x64.exe"; Parameters: "/quiet /install"; Check: NeedsVC

[Code]
function NeedsVC: Boolean;
begin
  Result := not RegKeyExists(HKLM, 'Software\Microsoft\VisualStudio\14.0\VC\Runtimes\x64');
end;
