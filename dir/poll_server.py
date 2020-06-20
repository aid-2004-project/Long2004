from socket import *
from select import *

sock = socket()
sock.bind(("0.0.0.0",8008))
sock.listen(5)
sock.setblocking(False)

p = poll()
p.register(sock,POLLIN)
connections = {}
while True:
    events = p.poll()
    for fd ,event in events:
        if fd == sock:
            conn ,addr = sock.accept()
            print("connect from ",addr)
            conn.setblocking(False)
            p.register(conn,POLLIN|POLLERR)
            connections[fd]=conn
        elif event == POLLIN:
            connfd = connections[fd]
            data = connfd.recv(1024)
            if not data:
                p.unregister(connfd)
                connfd.close()
                del connections[fd]
                continue
            print(data.decode())
            connfd.send(b"OK")

