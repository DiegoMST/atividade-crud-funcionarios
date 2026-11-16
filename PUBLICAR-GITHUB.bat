@echo off
setlocal
cd /d "%~dp0"
title Publicar projeto no GitHub
echo ============================================
echo  PUBLICAR NO GITHUB - CRUD DE FUNCIONARIOS
echo ============================================
echo.
where git >nul 2>nul
if errorlevel 1 (
    echo Git nao encontrado. Instale em https://git-scm.com/downloads/win
    pause
    exit /b 1
)
echo ANTES DE CONTINUAR:
echo 1. Preencha os nomes dos integrantes no README.md.
echo 2. Crie um repositorio PUBLICO e VAZIO no GitHub com o nome:
echo    atividade-crud-funcionarios
echo 3. Confira se nao colocou senhas reais nem dados pessoais no projeto.
echo.
set /p "USUARIO=Digite seu usuario do GitHub: "
if "%USUARIO%"=="" (
    echo Usuario vazio. Cancelado.
    pause
    exit /b 1
)
echo.
git init
if errorlevel 1 goto :erro
git add .
if errorlevel 1 goto :erro
git diff --cached --stat
echo.
set /p "CONFIRMA=Confirma que revisou os arquivos acima? (S/N): "
if /I not "%CONFIRMA%"=="S" (
    echo Envio cancelado.
    pause
    exit /b 0
)
git commit -m "Atividade Avaliativa 2 - CRUD de funcionarios"
if errorlevel 1 (
    echo O commit nao foi feito. Verifique git config user.name e git config user.email.
    pause
    exit /b 1
)
git branch -M main
git remote get-url origin >nul 2>nul
if not errorlevel 1 (
    echo Ja existe um remote origin configurado. Verifique com: git remote -v
    echo Nenhum remote foi alterado automaticamente.
    pause
    exit /b 1
)
git remote add origin "https://github.com/%USUARIO%/atividade-crud-funcionarios.git"
if errorlevel 1 goto :erro
git push -u origin main
if errorlevel 1 goto :erro
echo.
echo Publicacao enviada. Confirme no navegador se o repositorio esta PUBLICO.
echo https://github.com/%USUARIO%/atividade-crud-funcionarios
pause
exit /b 0
:erro
echo.
echo Falha ao enviar. Confira a autenticacao e o repositorio criado no GitHub.
pause
exit /b 1
