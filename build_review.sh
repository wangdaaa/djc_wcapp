#!/bin/sh
#review环境的build文件
REV=`git rev-parse --short HEAD`
#docker build -t djc:${REV} -f /data/djc_wcapp/Dockerfile1 . #dev
docker build -t review_djc:${REV} -f /data/djc_wcapp/Dockerfile1 . #review
CONTAINER_ID=$(docker ps -a|grep 9002|awk '{print $1}')#review使用9002端口
docker stop ${CONTAINER_ID};docker rm -f ${CONTAINER_ID}
docker run -itd -p9002:9001  -v /data/test/static/media:/root/static/media  review_djc:${REV}#review
