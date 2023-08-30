#!/bin/sh
docker run -e TZ=Europe/Berlin --env-file env.list python-imagename
