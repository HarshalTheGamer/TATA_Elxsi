@echo off
title AERO-SHIELD Prototype Launcher
cd /d "%~dp0"

echo ======================================================================
echo           AERO-SHIELD // CONNECTED FLEET AUTONOMICS
echo           Launching High-Fidelity Glassmorphic Web Prototype...
echo ======================================================================

:: Check if server is already running on port 8085
netstat -ano | findstr :8085 | findstr LISTENING >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo [INFO] Prototype server is already running on port 8085.
    goto OPEN_BROWSER
)

echo [1/2] Starting lightweight local server on http://localhost:8085/...
start /B "" python "%~dp0prototype\server.py" >nul 2>&1
ping -n 2 127.0.0.1 >nul 2>&1

:OPEN_BROWSER
echo [2/2] Opening dashboard in default web browser...
start http://localhost:8085/

echo.
echo ======================================================================
echo  [SUCCESS] AERO-SHIELD Prototype is live at: http://localhost:8085/
echo  To stop the server anytime, double-click STOP_PROTOTYPE.bat
echo ======================================================================
ping -n 2 127.0.0.1 >nul 2>&1
exit /b 0
