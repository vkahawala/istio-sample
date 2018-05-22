#!/usr/bin/env bash

kubectl delete -f transport-bus-service/busService.yaml
kubectl delete -f transport-time-service/timeService.yaml
kubectl delete -f transport-service/transportService.yaml
kubectl delete -f kube-res/whitelist-transport-service-for-bus-service.yaml