
import socket
from select import *

host = '172.40.72.237'
port =11118
address=(host,port)
server=socket.socket()
server.bind(address)
server.listen(10)
print('服务器已经启动！')
print(address)

user_list={server.fileno():server}
p=poll()
p.register(server,POLLIN|POLLOUT)



def send_all(fd,data):
    for sock in user_list.values():
        if sock is server:
            continue
        else:
            sock.send(data)
    return

def send_to_self(fd,data):
    user_list[fd].send(data)


def accept_conn(fd):
    client,addr=server.accept()
    print('客户端已连接：',addr)
    p.register(client,POLLIN)
    user_list[client.fileno()]=client

def read_conn(fd):
    sock=user_list[fd]

    try:
    
        data=sock.recv(1024)

        msg=data.decode()
        confirm_list=msg.split('::')


        if not data:
            p.unregister(sock)
            sock.close()
            del sock
        else:
            print('收到数据：',confirm_list)

            if confirm_list[0]=='login':#登录操作

                if confirm_list[1] == 'caicai' and confirm_list[2]=='123456':
                    respond='login::OK'
                else:
                    respond='login::NO'
                send_all(fd,respond.encode())

            elif confirm_list[0]=='rigister':
                pass
            
            elif confirm_list[0]=='multiChat':

                respond='multiChat::%s::%s'% (confirm_list[1],confirm_list[2])
                send_all(fd,respond.encode())

            elif confirm_list[0]=='singleChat':
                pass

            elif confirm_list[0]=='caicaiChat':

                print('接收到发送给菜菜的数据！',confirm_list[1])

                def get_computer(info):
                    url="http://www.tuling123.com/openapi/api?key=45b6072214a444d6b9cd348b1457b3a8&info="+info
                    try:
                        response =requests.get(url)
                    except Exception:
                        return '哎呀，网络服务器开小差了，召唤小菜菜失败...'

                    response.encoding = 'utf-8'
                    try:
                        dic_json = json.loads(response.text)
                    except Exception:
                        return '哎呀，网络服务器开小差了，召唤小菜菜失败...'
                    return dic_json['text']


                feedback=get_computer(confirm_list[1])
                respond='caicaiChat::%s' % feedback
                send_to_self(fd,respond.encode())
            
            return
    except Exception:
        pass

if __name__ == '__main__':
    while True:
        events=p.poll()
        for fd,e in events:
            if fd==server.fileno():
                accept_conn(fd)

            elif e & POLLIN:
                read_conn(fd)

    server.close()
    print('服务器退出！')