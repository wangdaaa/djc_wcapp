FROM python:3.6
WORKDIR /root
COPY . /root/
RUN pip install --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple -r /root/requirements.txt
CMD uwsgi --ini /root/iam_uwsgi.ini

