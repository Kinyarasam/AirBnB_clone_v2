#!/usr/bin/env bash
# Script that configures Nginx server with folders and files.

CUSTOM_HTML=\
"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

apt-get -y update
apt-get -y install nginx
service nginx start 
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "${CUSTOM_HTML}" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R "${USER}":"${USER}" /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
