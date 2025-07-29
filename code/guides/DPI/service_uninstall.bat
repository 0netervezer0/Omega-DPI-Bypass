@echo off
chcp 65001 >nul
:: 65001 - UTF-8

:: Admin rights check
pause

set SRVCNAME=Omega

net stop %SRVCNAME%
sc delete %SRVCNAME%

net stop "WinDivert"
sc delete "WinDivert"
net stop "WinDivert14"
sc delete "WinDivert14"

echo:
echo:
echo Service removed

pause
