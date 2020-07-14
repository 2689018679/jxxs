import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
print('正在连接服务器')
while True:
    con = input('请输入要发送的内容：')
    s.send(con.encode('utf-8'))
    if con=='out':
        print('结束')
        break
    res=s.recv(1024).decode('utf-8')
    print('接受到服务端:{}'.format(res))