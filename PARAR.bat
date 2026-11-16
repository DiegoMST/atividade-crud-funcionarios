@echo off
cd /d "%~dp0"
docker compose down
if errorlevel 1 (
  echo Falha ao parar. Confira se o Docker Desktop esta aberto.
) else (
  echo Sistema parado. Os dados cadastrados foram mantidos.
)
pause
