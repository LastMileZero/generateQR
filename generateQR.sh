#!/bin/bash
SCRIPTPATH=$(dirname $0)
if [[ ${SCRIPTPATH} = "." ]]; then
  SCRIPTPATH=$(pwd)
fi
cd "${SCRIPTPATH}/" || exit
if [[ ! -d ./env ]]; then
    ./make.sh
fi
# Lo activamos
source env/bin/activate
# Ejecutamos la sincronización
python3 exportSprint.py "$@"
# Desactivamos el enviroment
deactivate