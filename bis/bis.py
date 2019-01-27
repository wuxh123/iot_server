from common import gl
import os

filename=os.path.basename(os.path.realpath(__file__))

def parseDevData(map):
    print('#'*50)
    fd=map['fd']
    data=map['data']
    print(fd)
    print(data)
    split1=data.decode('gbk').split('*')
    print(split1)
    if (len(split1)==4):
        no = split1[0]
        id = split1[1]
        if (split1[0] not in gl.cs):
            gl.log.error(filename+",id={},no={},厂商配置编号错误.".format(id,no))
            return
        else:
            #todo 从db中判断，该id号是否属于该系统
            ismyid=True
            if ismyid:
                gl.dev_to_fd[id]=fd
                _len=int(split1[2])
                content=split1[3]
                contents=content.split(',')
                if contents[0]=='LK':
                    gl.fd_to_socket[fd].send(data)
                    gl.log.debug(filename+",id={},recived heartbeat > send heartbeat.".format(id))
                else:
                    gl.mqtt_client.publish(gl.mqtt_up,data)
                    gl.log.debug(filename+",id={},send to mqtt success.".format(id))
            else:
                gl.log.error(filename+"invalid connection.")

    else:
        gl.log.error(filename+"invalid data.")

def parseMqttData(map):
    #topic=map['topic']
    data=map['data']
    split1=data.decode('gbk').split('*')
    print(split1)
    if (len(split1)==4):
        no = split1[0]
        id=split1[1]
        if (split1[0] not in gl.cs):
            gl.log.error(filename+",id={},no={},厂商配置编号错误.".format(id,no))
            return
        else:
            #从gl.dev_to_fd中判断，该id是否上线
            if id in gl.dev_to_fd:
                fd=gl.dev_to_fd[id]
                print(fd)
                print(gl.fd_to_socket[fd])
                gl.fd_to_socket[fd].send(data)
                gl.log.debug(filename+",id={},send to device success.".format(id))
            else:
                gl.log.error(filename+",id={},not connected.".format(id))

    else:
         gl.log.error(filename+",id={},recv invalid data.".format(id))