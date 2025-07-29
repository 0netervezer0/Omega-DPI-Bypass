@echo off
chcp 65001 >nul
:: 65001 - UTF-8

cd /d "%~dp0"

set BIN=%~dp0bin\

start "DPI Bypass Terminal" /min "%BIN%winws.exe" ^
--wf-tcp=80,443 --wf-udp=443 ^
--filter-tcp=80 --hostlist="lists/list-general.txt" --dpi-desync=fake,split2 --dpi-desync-fooling=md5sig --dpi-desync-ttl=7 --new ^
--filter-tcp=443 --hostlist-auto="lists/list-general.txt" --hostlist-exclude="lists/list-general.txt" --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-ttl=4
