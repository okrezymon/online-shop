FROM php:7.1-apache
# Install.
RUN \
sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y build-essential && \
apt-get install -y software-properties-common && \
apt-get install -y byobu curl git htop man unzip vim wget && \
rm -rf /var/lib/apt/lists/*
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get upgrade
RUN mkdir -p /var/www/html/kursy-online/var/cache && mkdir -p /var/www/html/kursy-online/var/logs
COPY --chown=www-data:www-data ./prestashop /var/www/html/kursy-online
COPY ./server.crt /etc/apache2/sites-available
COPY ./server.key /etc/apache2/sites-available
COPY ./config/presta.conf /etc/apache2/sites-available/000-default.conf
RUN chown -R www-data:www-data /var/www/html/kursy-online/var
RUN chmod 777 /var/www/html/kursy-online/var/cache && chmod 777 /var/www/html/kursy-online/var/logs
RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable pdo_mysql
RUN a2enmod rewrite
# Define working directory.
WORKDIR /var/www/html
# Define default command.
RUN a2enmod ssl
RUN service apache2 restart
EXPOSE 80
EXPOSE 443
CMD apachectl -D FOREGROUND