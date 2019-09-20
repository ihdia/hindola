#!/bin/bash

mysql -u ${DB_USER} -p ${DB_NAME} < /save/dump.sql 