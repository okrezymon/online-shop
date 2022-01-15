#!/bin/bash

SQL_CONTAINER="online-shop_mysql-prestashop_1"
docker cp ./BE_158817.sql $SQL_CONTAINER:/tmp/BE_158817.sql
docker cp ./db_create.sh $SQL_CONTAINER:/tmp/db_create.sh
docker exec -it $SQL_CONTAINER  chmod 777 /tmp/db_create.sh
docker exec -it $SQL_CONTAINER /bin/sh /tmp/db_create.sh

