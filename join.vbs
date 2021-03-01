Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\[Replace with your path]\start.cmd" & Chr(34), 0
Set WshShell = Nothing
