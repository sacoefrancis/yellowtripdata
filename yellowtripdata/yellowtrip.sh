#!/usr/bin/env bash
set -e
echo "checking for image"
if [ ! -z $(docker ps -a -q --filter ancestor=postgres) ]; then
    docker stop $(docker ps -a -q --filter ancestor=postgres) 
fi
echo "installing postgres"
docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres 
docker exec -it pg-docker /bin/sh -c "apt-get update;apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8;apt install postgresql-client-common;apt install postgresql-client-10" 





