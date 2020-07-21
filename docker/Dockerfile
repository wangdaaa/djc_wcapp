FROM python:3.7.7-alpine3.10
WORKDIR /tmp
COPY ../requirements.txt /tmp
#需要对pip更新并安装 wheel 否则无法正常安装 msyqlclient
RUN pip3 install --upgrade pip\
    &&pip3 install wheel\
    &&pip3 install --upgrade setuptools\
    &&pip3 install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r /tmp/requirements.txt
# 需要删除项目引用文件的弟36 37 行 否则会报错 mysql clinet
RUN sed -i '36,37d'  /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/base.py
#cmd 命令只执行一个  只有一个有效
