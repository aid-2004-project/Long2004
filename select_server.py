"""
重点代码
思路：
要关注的io：监听套接字，各个客户端连接套接字

master分支测试
abby分支测试
"""
from socket import *
from select import select

# 创建监听套接字
sock = socket()
sock.bind(("0.0.0.0", 8008))
sock.listen(5)
sock.setblocking(False)
# 设置关注列表
rlist = [sock]  # 初始我们只关注监听套接字
wlist = []
xlist = []

# 对io进行关注
while True:
    rs, ws, xs = select(rlist, wlist, xlist)  # 当rlist中对象准备完毕后，rs列表会获取rlist中的对象
    # 准备完毕的意思值对象的可以执行任务，处于执行态，而不是在阻塞态
    # 对rs分情况讨论－－>sockfd一类：客户端链接　connfd一类：对应的客户端发消息
    for r in rs:  # 根据r的分类做判断，分别执行不同的行为
        if r is sock:
            connfd, addr = r.accept()
            print("connect from ", addr)
            # 每连接一个客户端，就将这个客户端连接套接字加入关注
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:  # 客户端退出处理
                rlist.remove(r)  # 不需要监控这个io
                r.close()
                continue
            print(data.decode())
            r.send(b"OK")
            wlist.append(r)
    for w in ws:
        w.send(b"OK")
        wlist.remove(w)
    for x in xs:
        pass
