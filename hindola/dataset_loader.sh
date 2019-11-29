#!/bin/bash
#ln -sn /data /main/myproject/static/imgdata
python3 service_tools/dataset_loader.py ${DB_USER} ${DB_PASS} ${DB_NAME} ${DB_HOST} /main/myproject/static/imgdata
