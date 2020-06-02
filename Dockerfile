FROM alpine
WORKDIR /root
COPY . /root/
MAINTAINER oyealex

# 定义需要的DJANGO版本
ENV DJANGO_VER 2.0

# 拷贝安装pip的脚本
COPY get-pip.py /get-pip.py

# 设置alpine的镜像地址为阿里云的地址
RUN echo "https://mirrors.aliyun.com/alpine/v3.6/main/" > /etc/apk/repositories \
    # 更新安装 bash curl python3等工具
    && apk update \
    && apk add --no-cache bash \
    # 修改为从本地文件拷贝此脚本，不再需要curl工具
    #    curl \
    python3 \
    # 由于通过apk安装的pip总是基于python2.7的版本，不符合项目要求，此处使用get-pip.py的方式
#安装基于python3.6的pip
    # 下载get-pip.py脚本
    # 从本地文件拷贝，不再下载
    #    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    # 安装pip
    && python3 /get-pip.py \
    # 从阿里云的镜像安装特定版本的django
    # 删除不必要的脚本
    && rm -f /get-pip.py \
    # 此环境专用做运行django项目，因此移除不必要的工具，减少空间
    && python3 -m pip uninstall -y pip setuptools wheel \
    && apk del curl \
    && pip install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r /root/requirements.txt
    # 最后清空apk安装时产生的无用文件
CMD uwsgi --ini /root/djc_uwsgi.ini  #通过uwsgi的方式启动django项目

