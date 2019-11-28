#!/bin/bash

python3 service_tools/queue.py &
#QUEUE = $(echo $!)
#export QUEUE
python3 Instance-segmentation-master/main/doc/modeltest.py &
#INSTSEG = $(echo $!)
#export INSTSEG
python3 semi-automatic/toolscrpt2.py &
#BBOX = $(echo $!)
#export BBOX
python3 main/app.py ${DB_USER} ${DB_PASS} ${DB_NAME} ${DB_HOST} ${APP_HOST} ${DATASET_LOC} &
#FLASKAPP = $(echo $!)
#export FLASKAPP
