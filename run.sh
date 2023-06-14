#!/bin/bash
printf "\033[1;32m"
echo "Stockholm in a Docker container"

sleep 2

cat ./services/ascii-art.txt

printf "\033[1;32m"
echo "Execute ./acces.sh in other bash tab to access it.
The infection folder is mounted at /home/stockholm/test,
so you can easily view the status of the files on the host."

sleep infinity
while true; do sleep 1; done