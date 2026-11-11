@echo off
cd /d "%~dp0"
set "PY=python"
where py >nul 2>nul
if %errorlevel%==0 set "PY=py"
%PY% --version >nul 2>nul
if not %errorlevel%==0 (
  echo Python nao encontrado.
  echo Instale em https://www.python.org/downloads/ e marque "Add python.exe to PATH".
  pause
  exit /b 1
)
echo Instalando o Meu Estudio...
%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt
if not %errorlevel%==0 (
  echo Algo deu errado na instalacao. Copie a mensagem acima e mande para o Claude.
  pause
  exit /b 1
)
echo.
echo Pronto! Agora de dois cliques em iniciar.bat
pause
