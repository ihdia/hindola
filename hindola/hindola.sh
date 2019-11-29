#!/bin/sh

echo "Enter the absolute path to your dataset directory."
read datasetdir
echo "Enter the IP of your machine on the network you are connected to."
read hostip

cd ..
cd ./save

HINDOLA_SAVE_DIR="$(pwd)"

cd ../hindola/

#cat ./docker-compose-config | sed 's#HINDOLA_SAVE_DIR#'"${HINDOLA_SAVE_DIR}"'#g' | sed 's#HINDOLA_DATA_DIR#'"${datasetdir}"'#g' > docker-compose.yml
#docker-compose up --build

docker build -t hindola/local:latest .
docker run -it -d --network host --runtime=nvidia --name hindola -e DB_USER=root -e DB_PASS=root -e DB_NAME=annotation_web -e DB_HOST=localhost -e APP_HOST=${hostip} -e DATASET_LOC=${datasetdir} $(ls -la /dev | grep nvidia | sed 's/\s\s*/ /g' | cut -d ' ' -f 10 | while read -r line; do echo "--device /dev/$line:/dev/$line"; done | tr '\n' ' ') -v "${HINDOLA_SAVE_DIR}:/save" -v "${datasetdir}:/data" -p ${hostip}:10000:10000 hindola/local /bin/bash
docker exec -it -d $(docker ps -aqf "name=hindola") mysqld_safe --user=mysql
docker exec $(docker ps -aqf "name=hindola") ./app_config.sh
docker exec $(docker ps -aqf "name=hindola") ln -sn /data /main/myproject/static/imgdata
docker exec -it $(docker ps -aqf "name=hindola") bash 
