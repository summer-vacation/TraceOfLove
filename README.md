## TraceOfLove

前后端分离 backend 使用flask框架，代码置于backend文件夹下，前端使用vue框架，代码置于frontend文件夹下。

### backend
环境：  
python 3.7 64位


说明：  
1. 需要的一些python库 > requirements.txt  
  &nbsp; 一键安装方法：  
  &nbsp;&nbsp;&nbsp; pip install -r requirements.txt
   
2. run.py中有一段测试代码，可以运行

发布：
centos7下通过uwsgi+Nginx发布Flask应用

(uWSGI: micro web server gateway interface)

安装uwsgi: pip install uWSGI 

配置uwsgi:

编写uwsgi config文件; 
cmd : uwsgi -ini [path to uwsgi_config_file];

配置nginx:

编写nginx config文件
cmd : nginx -c [path to nginx config file]


nginx 代理上层请求，处理部分静态请求、负载均衡（并没有多个服务器），限制过载请求，传递其他请求到uwsgi层;

uwsgi托管flask项目，其作用为：
* 消息路由
* 允许在一个进程中同时运行多个应用程序或者应用框架
* 负载均衡和rpc
* 中间层内容处理

重启服务 uwsgi --reload [uwsgi config file]

### frontend
环境:
nodejs v12.4.0
npm 6.9.0
vue 2.9.6
