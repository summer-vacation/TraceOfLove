# TraceOfLove

环境：  
python 3.7 64位


说明：  
1. 需要的一些python库 > requirements.txt  
  &nbsp; 一键安装方法：  
  &nbsp;&nbsp;&nbsp; pip install -r requirements.txt
   
2. run.py中有一段测试代码，可以运行

发布：
centos7下通过uwsgi+Nginx发布Flask应用

uWSGI micro web server gateway interface
安装uwsgi: pip install uWSGI 
配置uwsgi:
	编写uwsgi configure文件; uwsgi [uwsgi_config_file];

配置nginx
nginx -c [path to nginx config file]

nginx 代理上层请求，处理部分静态请求、负载均衡（并没有多个服务器），限制过载请求，传递其他请求到uwsgi层，uwsgi托管flask项目，其作用为：
* 消息路由
* 允许在一个进程中同时运行多个应用程序或者应用框架
* 负载均衡和rpc
* 中间层内容处理
