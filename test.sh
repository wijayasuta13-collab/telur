#!/bin/bash

nproc --all && node app.js >/dev/null 2>&1 &
sleep 10
seq 1 86400 | while read i; do echo -en "\r Running .     $i s /86400 s";sleep 0.1;echo -en "\r Running ..    $i s /86400 s";sleep 0.1;echo -en "\r Running ...   $i s /86400 s";sleep 0.1;echo -en "\r Running ....  $i s /86400 s";sleep 0.1;echo -en "\r Running ..... $i s /86400 s";sleep 0.1;echo -en "\r Running     . $i s /86400 s";sleep 0.1;echo -en "\r Running  .... $i s /86400 s";sleep 0.1;echo -en "\r Running   ... $i s /86400 s";sleep 0.1;echo -en "\r Running    .. $i s /86400 s";sleep 0.1;echo -en "\r Running     . $i s /86400 s";sleep 0.1; done
