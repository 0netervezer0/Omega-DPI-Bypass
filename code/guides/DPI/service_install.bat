@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul

echo Press Enter to confirm the creation of the service.
pause
cls

cd /d "%~dp0"

set BIN_PATH=%~dp0bin\


set "count=0"
for %%f in (*.bat) do (
    set "filename=%%~nxf"
    if /i not "!filename:~0,7!"=="service" (
        set /a count+=1
        echo !count!. %%f
        set "file!count!=%%f"
    )
)


set "choice="
echo:
echo For default installation in Russia enter 12
echo For default installation in Iran enter 13
set /p "choice=Enter the file number: "

if "!choice!"=="" goto :eof

set "selectedFile=!file%choice%!"


set "args="
set "capture=0"
set "mergeargs=0"
set QUOTE="

for /f "tokens=*" %%a in ('type "!selectedFile!"') do (
    set "line=%%a"

    echo !line! | findstr /i "%BIN%winws.exe" >nul
    if not errorlevel 1 (
        set "capture=1"
    )

    if !capture!==1 (
        if not defined args (
            set "line=!line:*%BIN%winws.exe"=!"
        )

        set "temp_args="
        for %%i in (!line!) do (
            set "arg=%%i"

            if not "!arg!"=="^" (
                if "!arg:~0,2!" EQU "--" if not !mergeargs!==0 (
                    set "mergeargs=0"
                )

                if "!arg:~0,1!" EQU "!QUOTE!" (
                    set "arg=!arg:~1,-1!"

                    echo !arg! | findstr ":" >nul
                    if !errorlevel!==0 (
                        set "arg=\!QUOTE!!arg!\!QUOTE!"
                    ) else if "!arg:~0,1!"=="@" (
                        set "arg=\!QUOTE!@%~dp0!arg:~1!\!QUOTE!"
                    ) else if "!arg:~0,5!"=="%%BIN%%" (
                        set "arg=\!QUOTE!!BIN_PATH!!arg:~5!\!QUOTE!"
                    ) else (
                        set "arg=\!QUOTE!%~dp0!arg!\!QUOTE!"
                    )
                )
                
                if !mergeargs!==1 (
                    set "temp_args=!temp_args!,!arg!"
                ) else (
                    set "temp_args=!temp_args! !arg!"
                )

                if "!arg:~0,4!" EQU "--wf" (
                    set "mergeargs=2"
                ) else if "!arg!" EQU "--dpi-desync" (
                    set "mergeargs=2"
                ) else if "!arg!" EQU "--dpi-desync-fooling" (
                    set "mergeargs=2"
                ) else if !mergeargs!==2 (
                    set "mergeargs=1"
                )
            )
        )

        if not "!temp_args!"=="" (
            set "args=!args! !temp_args!"
        )
    )
)


set ARGS=%args%
echo Final args: !ARGS!

set SRVCNAME=Omega

net stop %SRVCNAME%
sc delete %SRVCNAME%
sc create %SRVCNAME% binPath= "\"%BIN_PATH%winws.exe\" %ARGS%" DisplayName= "Omega" start= auto
sc description %SRVCNAME% "Omega DPI Bypass Software"
sc start %SRVCNAME%

echo:
echo:
echo Service Installed!

pause