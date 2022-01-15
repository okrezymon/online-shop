#!/bin/bash

mysql -pstudent -e "DROP DATABASE IF EXISTS BE_158817;"
mysql -pstudent -e "CREATE DATABASE BE_158817;"
mysql -pstudent -e "USE BE_158817;"
mysql -pstudent -e "CREATE USER IF NOT EXISTS BE_158817@'%' IDENTIFIED BY 'student';"
mysql -pstudent -e "GRANT ALL PRIVILEGES ON BE_158817.* TO 'BE_158817'@'%';"
mysql -pstudent -e "FLUSH PRIVILEGES;"
mysql -u BE_158817 -pstudent BE_158817 < /tmp/BE_158817.sql
mysql -u BE_158817 -pstudent BE_158817 -e "UPDATE ps_shop_url SET domain='localhost:58817', domain_ssl='localhost:58817' WHERE id_shop_url=1;"