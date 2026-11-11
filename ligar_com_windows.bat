@echo off
cd /d "%~dp0"
set "PYW=pythonw"
where pyw >nul 2>nul
if %errorlevel%==0 set "PYW=pyw"
set "ATALHO=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\MeuEstudio.bat"
(
  echo @echo off
  echo cd /d "%~dp0"
  echo start "" %PYW% app.py --sem-navegador
) > "%ATALHO%"
echo Pronto! O Meu Estudio vai abrir escondido sempre que o PC ligar.
echo Para usar, abra http://localhost:5252 no navegador (ou de dois cliques em iniciar.bat).
echo Para desligar isso, use desligar_do_windows.bat
pause
