#!/bin/bash

# Leer la IP pública desde el archivo
IP=$(cat ~/abm-de-usuarios/public_ip.txt)

# Verificar si la IP está vacía
if [ -z "$IP" ]; then
    echo "El archivo public_ip.txt está vacío. No se puede actualizar la configuración de Nginx."
    exit 1
fi

# Crear o actualizar el archivo de configuración de Nginx
cat <<EOL | sudo tee /etc/nginx/sites-available/abm-de-usuarios
server {
    listen 80;
    server_name $IP;  # Usa la IP pública leída del archivo

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/abm-de-usuarios;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/abm-de-usuarios/gunicorn.sock;
    }
}
EOL

# Crear un enlace simbólico para habilitar la configuración
sudo ln -sf /etc/nginx/sites-available/abm-de-usuarios /etc/nginx/sites-enabled

# Verificar la configuración de Nginx y reiniciar el servicio
sudo nginx -t
sudo systemctl restart nginx
