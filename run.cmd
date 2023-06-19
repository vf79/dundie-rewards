@ echo off

chcp 65001
set name="dundie-rewards"

if "%1"=="--clean" goto clean
goto help

:clean
    echo "Excluindo arquivos e diretorios desnecessários..."
    for /r . %%f in (*.pyc) do @if exist "%%f" del "%%f"
    goto end

:help
    echo "Utilize .\run.cmd --<parametro>"
    echo "Parâmetros:"
    echo "clean - Limpa o codigo"

:end
    echo "Script finalizado."