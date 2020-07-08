FROM python:3.6
WORKDIR /root
COPY . /root/
#需要对pip更新并安装 wheel 否则无法正常安装 msyqlclient
RUN pip3 install -r /root/requirements.txt  --cache-dir /pip-cache
#需要删除项目引用文件的弟36 37 行 否则会报错 mysql clinet
RUN sed -i '36,37d'  /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/base.py

# 拷贝安装pip的脚本
#COPY get-pip.py /get-pip.py

#cmd 命令只执行一个  只有一个有效
CMD uwsgi --ini /root/djc_uwsgi1.ini
