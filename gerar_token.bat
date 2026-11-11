@echo off
cd /d "%~dp0"
set "PY=python"
where py >nul 2>nul
if %errorlevel%==0 set "PY=py"
%PY% gerar_token.py
pause
