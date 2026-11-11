@echo off
cd /d "%~dp0"
set "PY=python"
where py >nul 2>nul
if %errorlevel%==0 set "PY=py"
echo Abrindo o Meu Estudio em http://localhost:5252
echo Deixe esta janela aberta (pode minimizar). Fechar a janela desliga o app.
echo.
%PY% app.py
pause
