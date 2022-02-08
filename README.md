0.迁移数据库
数据来源MySQL
需要使用MySQL数据库
由于Django只支持表级操作，需要先手动创建数据库：mall（utf8mb4字符集）
执行以下代码迁移数据库：
python manage.py makemigrations
python manage.py migrate
然后执行SQL文件插入数据

1.启动服务器端要使用
python manage.py runserver 0.0.0.0:8088
因为前端会按照这个接口来调用

2.前端页面中写的IP地址要修改为你自己的IP地址
在mall_vue/src/api/http.js  文件中，端口只要和服务器一致即可

3.服务器端是mall_py，使用pycham打开
   前端是mall_vue，使用vue ui打开控制台网页版，加载项目后运行即可

项目正在开发中...
目前综合页面已开发完成
