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
 
 2.Iot server保存设备id
 
 3.通过设备id订阅该设备的消息
 
 4.中心通过该设备的定于发送指令
 
 5.通过该server，将mqtt指令转发给具体的socket，实现数据透明传输。
 
 
 ## 特点
 1.采用epoll+线程池处理指令，此处如果为cpu密集型操作，可以改成进程池
 
 2.采用mqtt+threadpoll 处理指令。
 
 ## 其他
 通过模拟多device操作，每毫秒发送数据，未发生数据丢失，粘包。cpu负荷在5%以下。
 
 ## 运行
 python main.py
 
 ## 测试
 python test.py
 
 ## 其他
 1.如果觉得python性能不够好（我觉得不错的），可以改为pypy
 
 2.数据粘包比较麻烦，我测试过，如果线程池是20，每毫秒3条数据会粘包。线程池50的话就没有发生粘包。
 
 ## 设备A通过epoll链接到iot server，server将其注册到mqtt broker
 ![img](https://github.com/wuxh123/iot_server/blob/master/img/1.jpg)
 
  ## 设备B通过epoll链接到iot server，server将其注册到mqtt broker
 ![img](https://github.com/wuxh123/iot_server/blob/master/img/2.jpg)
 
  ## 每毫秒设备A和设备2同时向iot server发送指令，指令转送给 mqttbroker。没有丢包，没有延时
 ![img](https://github.com/wuxh123/iot_server/blob/master/img/3.jpg)
 
   ## 设备A通过mqtt向设备B发送指令
 ![img](https://github.com/wuxh123/iot_server/blob/master/img/4.jpg)
