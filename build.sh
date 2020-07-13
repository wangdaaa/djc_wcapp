#!/bin/sh
#dev环境的build文件
REV=`git rev-parse --short HEAD`
docker build -t djc:${REV} -f /data/djc_wcapp/Dockerfile1 .
CONTAINER_ID=$(docker ps -a|grep 9001|awk '{print $1}')
docker stop ${CONTAINER_ID};docker rm -f ${CONTAINER_ID}
docker run -itd -p9001:9001  -v /data/test/static/media:/root/static/media  djc:${REV}
#docker run -itd -p9001:9001  -v /data/test/static/media:/root/static/media  -v $HOME/.cache/pip/:/pip-cache  djc:${REV}
