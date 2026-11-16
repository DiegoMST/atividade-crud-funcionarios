@echo off
setlocal
cd /d "%~dp0"
title Verificar CRUD
echo Verificando os servicos...
docker compose ps
if errorlevel 1 goto :erro
echo.
echo Conferindo configuracao Django...
docker compose exec -T sistema python manage.py check
if errorlevel 1 goto :erro
echo.
echo Executando os testes automatizados do CRUD...
docker compose exec -T -e TEST_USE_SQLITE=1 sistema python manage.py test app
if errorlevel 1 goto :erro
echo.
echo Verificacoes concluidas com sucesso.
pause
exit /b 0
:erro
echo.
echo Alguma verificacao falhou. Consulte a mensagem acima.
pause
exit /b 1
