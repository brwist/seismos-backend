#!/usr/bin/env bash
sudo docker-compose stop seismos_backend_api
sudo docker-compose rm -f seismos_backend_api
sudo docker-compose pull seismos_backend_api
sudo docker-compose up seismos_backend_api
