#!/bin/bash

docker-compose up -d

echo "waiting for the containers to start..."
docker-compose ps

echo "Wating 30s"
sleep 30s

URL="http://0.0.0.0:8000"
echo "Open $URL"
xdg-open $URL
