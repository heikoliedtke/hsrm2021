FROM ubuntu:18.04

RUN apt-get update && apt-get install -y nginx

COPY ./ ./app

WORKDIR ./app

COPY hsrm.html /var/www/html/index.html

CMD ["nginx", "-g", "daemon off;"]



