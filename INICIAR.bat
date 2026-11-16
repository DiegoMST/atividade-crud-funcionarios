@echo off
setlocal
cd /d "%~dp0"
title Cadastro de Funcionarios - Inicializar
where docker >nul 2>nul
if errorlevel 1 (
  echo ERRO: Docker Desktop nao encontrado.
  echo Instale e abra o Docker Desktop antes de executar este arquivo.
  echo https://www.docker.com/products/docker-desktop/
  pause
  exit /b 1
)
docker info >nul 2>nul
if errorlevel 1 (
  echo ERRO: Docker Desktop nao esta em execucao.
  echo Abra o Docker Desktop e aguarde o mecanismo iniciar.
  pause
  exit /b 1
)
echo Preparando o sistema e o MySQL...
docker compose up -d --build
if errorlevel 1 (
  echo Falha ao iniciar. Verifique as mensagens acima.
  pause
  exit /b 1
)
echo.
echo Sistema iniciado. O banco e as tabelas sao preparados automaticamente.
echo Aguarde alguns instantes no primeiro acesso.
echo Endereco: http://127.0.0.1:8000/app/lista_funcionarios
start "" "http://127.0.0.1:8000/app/lista_funcionarios"
echo.
echo Para conferir o servidor: docker compose logs -f sistema
pause
