#!/bin/sh
#review环境的build文件
REV=`git rev-parse --short HEAD`
#docker build -t djc:${REV} -f /data/djc_wcapp/Dockerfile1 . #dev
docker build -t review_djc:${REV} -f /data/review_djc/djc_wcapp/Dockerfile_review .
CONTAINER_ID=$(docker ps -a|grep 9002|awk '{print $1}')
if  [ ! -z  $CONTAINER_ID ] ;then
  docker stop ${CONTAINER_ID};docker rm -f ${CONTAINER_ID}
fi
docker run -itd -p9002:9002  -v /data/test/static/media:/root/static/media  review_djc:${REV}
