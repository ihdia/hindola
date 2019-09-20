#!/bin/bash

mysqldump -u ${DB_USER} -p ${DB_NAME} > /save/dump.sql