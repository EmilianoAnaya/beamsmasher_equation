Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "App.bat" & chr(34), 0
Set WshShell = Nothing