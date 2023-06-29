@ echo off

chcp 65001
set name="dundie"


if "%1"=="--clean" goto clean
if "%1"=="--formate" goto formate
if "%1"=="--install" goto install
if "%1"=="--install-dev" goto install-dev
if "%1"=="--install-test" goto install-test
if "%1"=="--lint" goto lint
if "%1"=="--test" goto test
if "%1"=="--test-ci" goto test-ci
if "%1"=="--test-debug" goto test-debug
if "%1"=="--test-run" goto test-run
if "%1"=="--virtualenv" goto virtualenv
if "%1"=="--watch" goto watch

goto help

:clean
    echo "Excluindo arquivos e diretorios desnecessários..."
    for /r . %%f in (*.pyc) do @if exist "%%f" del "%%f"
    for /d /r . %%d in (__pycache__, *.egg-info, .pytest_cache) do @if exist "%%d" rd /s /q "%%d"
    rd /s /q build
goto end

:formate
    echo "Formatando codigo..."
    .\.venv\Scripts\python -m isort dundie tests integration
    .\.venv\Scripts\python -m black dundie tests integration
goto end

:install
    echo "Instalando dependências do projeto..."
    .\.venv\Scripts\python -m pip install -e .
goto end

:install-dev
    echo "Instalando dependências de desenvolvimento..."
    .\.venv\Scripts\python -m pip install -e ".[dev]"
goto end

:install-test
    echo "Instalando dependências de testes..."
    .\.venv\Scripts\python -m pip install -e ".[test]"
goto end

:lint
    echo "Verificando qualidade do codigo..."
    .\.venv\Scripts\python -m pflake8
goto end

:test
    echo "Executando testes..."
    ::pytest tests\ -vv --cov=%name%
    pytest -vv -s
    ::coverage html
goto end

:test-debug
    echo "Executando testes com debug..."
    pytest -vv --pdb --pdbcls=IPython.terminal.debugger:Pdb -s
goto end

:test-run
    echo "Executando testes selecionados..."
    if [%2]==[] goto test
    pytest -vv -s -m "%2"
goto end

:virtualenv
    echo "Instalando virtualenv..."
    .\.venv\Scripts\python -m venv .venv --upgrade-deps
goto end

:watch
    echo "Pytest Watch..."
    ptw -- -vv -s tests\
goto end

:help
    echo "Utilize .\run.cmd --<parametro>"
    echo "Parâmetros:"
    echo "clean - Limpa o codigo"
    echo "install - Instala dependências do projeto"
    echo "install-dev - Instala dependências de desenvolvimento"
    echo "install-test - Instala dependências de testes"
    echo "lint - Verifica a qualidade do codigo escrito"
    echo "test - Executa testes"
    echo "test-ci - Executa testes e gera relatório junit.xml"
    echo "test-debug - Executa testes com debub"
    echo "test-run - Executa testes com mark run"
    echo "watch - Executa teste usando pytest-watch"
    echo "virtualenv - Cria a virtualenv do python"

:end
    echo "Script finalizado."