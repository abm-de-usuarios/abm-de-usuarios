#!/bin/bash

# Obtiene la IP pública del servidor
CURRENT_IP=$(curl -s https://api.ipify.org)

# Guarda la IP en un archivo dentro del directorio abm-de-usuarios
echo $CURRENT_IP > ~/abm-de-usuarios/public_ip.txt
