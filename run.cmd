@ echo off

chcp 65001
set name="dundie"

if "%1"=="--clean" goto clean
goto help

:clean
    echo "Excluindo arquivos e diretorios desnecessários..."
    for /r . %%f in (*.pyc) do @if exist "%%f" del "%%f"
    for /d /r . %%d in (__pycache__, *.egg-info, .pytest_cache) do @if exist "%%d" rd /s /q "%%d"
    rd /s /q build
    goto end

:help
    echo "Utilize .\run.cmd --<parametro>"
    echo "Parâmetros:"
    echo "clean - Limpa o codigo"

:end
    echo "Script finalizado."