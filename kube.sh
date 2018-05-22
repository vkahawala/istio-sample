#!/usr/bin/env bash

kubectl create -f transport-bus-service/busService.yaml
kubectl create -f transport-time-service/timeService.yaml
kubectl create -f transport-service/transportService.yaml