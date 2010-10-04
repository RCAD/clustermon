REM THIS IS NO LONDER USED

@echo off
start /wait \\scholastic.ringling.edu\SYSVOL\scholastic.ringling.edu\Logon_Logoff_Scripts\sgi_logoff_script.exe
set cn_str=%computername:~0, 3%
if /i "%cn_str%" NEQ "sgi" goto :eof
ping -n 30 127.0.0.1 > nul