#!/bin/sh

echo "Enter the absolute path to your dataset directory."
read datasetdir

cd ..
cd ./save

HINDOLA_SAVE_DIR="$(pwd)"

cd ../hindola/

#cat ./docker-compose-config | sed 's#HINDOLA_SAVE_DIR#'"${HINDOLA_SAVE_DIR}"'#g' | sed 's#HINDOLA_DATA_DIR#'"${datasetdir}"'#g' > docker-compose.yml
#docker-compose up --build

docker build -t hindola/local:latest .
docker run -it -d --name hindola -e DB_USER=root -e DB_PASS=root -e DB_NAME=annotation_web -e DB_HOST=localhost -e APP_HOST=0.0.0.0 -e DATASET_LOC=${datasetdir} -v "${HINDOLA_SAVE_DIR}:/save" -v "${datasetdir}:/data" -p 10000:10000 hindola/local /bin/bash
docker exec -it -d $(docker ps -aqf "name=hindola") mysqld_safe --user=mysql
docker exec -it $(docker ps -aqf "name=hindola") bash