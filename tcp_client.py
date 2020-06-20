from socket import *



# 创建TCP套接字
sockfd = socket()
# 发起连接
sockfd.connect(("127.0.0.1", 9889))
# 向服务端发送消息
while True:
    msg = input(">>>")
    sockfd.send(msg.encode())
    # 接收服务端消息
    data = sockfd.recv(1024)
    print(data.decode())
# 关闭套接字
sockfd.close()
