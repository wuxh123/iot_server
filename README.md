# iot_server
利用epoll mqtt redis mysql mongodb 搭建的一个后台iot server的雏形。采用多进程的方式运行，提升cpu利用率。

## 开发工具
vs code

## vscode 插件
pip install pylint

## python库
 pip install mysql-connector
 
 pip install mysqlclient
 
 pip isntall paho-mqtt
 
 pip install protobuf
 
 pip install pymongo
 
 pip install redis
 
 ## 功能
 1.设备通过socket连接到服务器
 
 2.保存设备id
 
 3.通过mqtt发布到mqtt broker
 
 4.订阅该设备的消息
 
 5.中心通过该设备的定于发送指令
 
 6.通过该server，将mqtt指令转发给具体的socket，实现数据透明传输。
 
 
 ## 特点
 1.采用epoll+线程池处理指令，此处如果为cpu密集型操作，可以改成进程池
 
 2.采用mqtt+threadpoll 处理指令。
 
 ## 其他
 通过模拟多device操作，每毫秒发送数据，未发生数据丢失，粘包。cpu符合在5%以下。
  
 ## 先写说明之后上代码
 
