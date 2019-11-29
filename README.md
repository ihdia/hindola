# System Setup

## Pre-requisites:
+ Git LFS
+ Docker Engine

## Download Instructions
##### Run the following commands  
  
  
#### To install git lfs:

+ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
+ sudo apt-get install git-lfs
+ git lfs install

#### To clone the repository:

+ git lfs install --skip-smudge
+ git clone https://github.com/ihdia/hindola.git
+ git lfs pull
+ git lfs install --force

#### To install Docker:

Use the following link for detailed instructions on Docker installation: https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Running the Tool:
+ Go to hindola/hindola
+ If you want the GPU to be accessable through the docker container, then use the following link to install cuda and/or nvidia-docker2 libraries as necessary: https://devblogs.nvidia.com/gpu-containers-runtime/
+ Or remove "--runtime=nvidia" (without the quotes) from hindola.sh file, if you don't want the GPU.
+ Run ./hindola.sh
+ After this step, you'll be asked to enter the absolute path to your dataset folder. Type it out and hit enter. 
+ Now, you'll be asked to enter the IP of your machine on the network you are connected to. Type it out and hit enter. If you want to run this tool only locally on a machine, just type out "0.0.0.0" (without the quotes).

#### To load the dataset into the database:
+ Run ./dataset_loader.sh

#### To resume previously saved sessions:
+ If you have saved a session previously, run ./load.sh to resume.
+ Password is 'root'.

#### To start the system:
+ Run ./start.sh
+ Use the same IP you used before to login through port 10000 on your host computer browser.

#### To stop running the annotation tool:
+ Run ./stop.sh

#### To save the session and export the data:
+ Run ./save.sh
+ Password is 'root'.

#### To exit the docker container:
+ exit












