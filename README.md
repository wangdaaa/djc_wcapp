# djc_wcapp
a wechat app  djc_wcapp
#创建文件目录 用于挂载容器接收的文件保存到本地虚拟机
mkdir -p /data/test/static/media
#git 拉下项目之后  切换到dev 分支 并在目录下创建 static/media目录
#创建镜像
docker build -t djc:v10  -f /data/djc_wcapp/Dockerfile1 .
#依靠容器创建镜像   绑定端口 绑定volume地ss
docker run -itd -p9001:9001 --name djc_nb1  -v /data/test/static/media:/root/static/media   djc:v10


