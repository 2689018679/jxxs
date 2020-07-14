import socket,threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen(5)
print('服务器已启动')

def run(client,attr):
    print('{}已连接'.format(attr))
    while True:
        res=client.recv(1024).decode('utf-8')
        if res == 'out':
            print('{}已退出连接'.format(attr))
            break
        print('接受到客户端消息：{}'.format(res))
        msg='接受成功'
        client.send(msg.encode("utf-8"))
    client.close()

if __name__ == '__main__':
    while True:
        client,attr=s.accept()
        t=threading.Thread(target=run,args=(client,attr))
        t.start()
        t.join()

