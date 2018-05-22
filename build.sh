#!/usr/bin/env bash

ROOT=${PWD}
cd ${ROOT}/transport-bus-service/
docker build -t bus-service .

cd ${ROOT}/transport-time-service/
docker build -t time-service .

cd ${ROOT}/transport-service/
docker build -t transport-service .