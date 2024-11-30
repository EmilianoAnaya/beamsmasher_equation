@echo off
echo Creando un venv...
python -m venv .venv

echo Activando el entorno virtual...
call .venv\Scripts\activate

echo Instalando y actualizando paquetes...
python -m pip install --upgrade pip
pip install -r requierements.txt