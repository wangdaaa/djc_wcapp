# djc_wcapp
a wechat app  djc_wcapp
#创建文件目录 用于挂载容器接收的文件保存到本地虚拟机
mkdir -p /data/test/static/media
#git 拉下项目之后  切换到dev 分支 并在目录下创建 static/media目录
#容器启动
#创建镜像
docker build -t djc:v10  -f /data/djc_wcapp/Dockerfile1 .
#依靠容器创建镜像   绑定端口 绑定volume地ss
docker run -itd -p9001:9001 --name djc_nb1  -v /data/test/static/media:/root/static/media   djc:v10


#uwsig启动项目
#安装依赖
pip3 install -r requirements.txt
#测试是否依赖安装好并能正常启动项目
python3 manage.py runserver
#如果能正常启动的话，再使用uwsgi启动项目
# 使用uwsgi启动
uwsgi --ini djc_uwsgi.ini


#nginx服务器配置
在 /etc/nginx 中创建文件夹 cert
将https密钥文件放入此处
[root@djc_nb cert]# ll
-rw-r--r-- 1 root root 1679 Jul  7 18:16 4175468_www.daxingyouxijihe.com.key
-rw-r--r-- 1 root root 3708 Jul  7 18:16 4175468_www.daxingyouxijihe.com.pem
nginx配置文件设置好重启nginx服务
cd /usr/sbin
nginx -s reload
