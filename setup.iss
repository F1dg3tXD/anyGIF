[Setup]
AppName=anyGIF
AppVersion=0.0.2b
DefaultDirName={pf}\anyGIF
DefaultGroupName=anyGIF
OutputDir=.
OutputBaseFilename=anyGIF_0_0_2b
Compression=lzma
SolidCompression=yes
SetupIconFile=res\winIcon.ico

[Files]
Source: "bin\*"; DestDir: "{app}\bin"; Flags: ignoreversion recursesubdirs
Source: "dist\anyGIF.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "res\appIcon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "redist\VC_redist.x64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Icons]
Name: "{commondesktop}\anyGIF"; Filename: "{app}\anyGIF.exe"; WorkingDir: "{app}"
Name: "{userprograms}\anyGIF"; Filename: "{app}\anyGIF.exe"; WorkingDir: "{app}"

[Run]
Filename: "{tmp}\VC_redist.x64.exe"; Parameters: "/quiet /install"; Check: NeedsVC

[Code]
function NeedsVC: Boolean;
begin
  Result := not RegKeyExists(HKLM, 'Software\Microsoft\VisualStudio\14.0\VC\Runtimes\x64');
end;
