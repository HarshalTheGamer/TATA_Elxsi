@echo off
title Stopping AERO-SHIELD Prototype
cd /d "%~dp0"

echo ======================================================================
echo           AERO-SHIELD // Stopping Prototype Server...
echo ======================================================================

:: 1. Kill via PID file if present
if exist "%~dp0prototype\prototype.pid" (
    set /p PID=<"%~dp0prototype\prototype.pid"
    if defined PID (
        taskkill /F /PID %PID% >nul 2>&1
    )
    del /f /q "%~dp0prototype\prototype.pid" >nul 2>&1
)

:: 2. Kill any process listening on port 8085 via PowerShell
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8085 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }" >nul 2>&1

echo.
echo ======================================================================
echo  [SUCCESS] AERO-SHIELD Prototype server on port 8085 has been stopped.
echo ======================================================================
ping -n 2 127.0.0.1 >nul 2>&1
exit /b 0
