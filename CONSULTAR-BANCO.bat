@echo off
setlocal
cd /d "%~dp0"
title Consultar registros no MySQL
echo ===============================================
echo  CONSULTA DOS FUNCIONARIOS NO BANCO MYSQL
echo ===============================================
echo.
docker compose ps
if errorlevel 1 goto :erro
echo.
docker compose exec -T sistema python manage.py shell -c "exec(open('consultar_banco.py', encoding='utf-8').read())"
if errorlevel 1 goto :erro
echo.
echo A consulta acima executou SELECT diretamente no banco configurado pelo Django.
echo Cadastre, edite e exclua um funcionario e consulte novamente.
pause
exit /b 0
:erro
echo.
echo ERRO. Confira se o Docker Desktop e os containers estao iniciados.
echo Diagnostico: docker compose logs --tail=50 sistema banco
pause
exit /b 1
