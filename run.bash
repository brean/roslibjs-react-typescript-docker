#!/bin/bash
docker network create roslibpytest
terminator -l roslibpytest -g terminator.conf

# cleanup after the user closes the terminator window
docker-compose down
docker network rm roslibpytest