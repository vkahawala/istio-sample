#!/usr/bin/env bash

docker tag bus-service vkahawala/bus-service:latest
docker tag time-service vkahawala/time-service:latest
docker tag transport-service vkahawala/transport-service:latest


docker push vkahawala/bus-service:latest
docker push vkahawala/time-service:latest
docker push vkahawala/transport-service:latest

