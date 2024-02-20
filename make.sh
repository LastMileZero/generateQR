#!/bin/sh
# Script to Install
#
cd "$(dirname "$0")"
# Creamos el virtual enviroment
python3 -m venv env
# Actualizamos el env
pip install --upgrade pip virtualenv env
# Lo activamos
source env/bin/activate
# Le instalamos las librerias
pip install -r requirements.txt
deactivate
#Cambio los permisos del script
chmod 744 *.sh
