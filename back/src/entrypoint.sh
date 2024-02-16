#!/bin/bash

# Espera hasta que MySQL esté disponible
echo 'Esperando a que MySQL se inicie...'
sleep 10


# Ejecuta tu aplicación Python
python core/controller/app.py
