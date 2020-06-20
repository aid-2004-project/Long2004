import time
from socket import *

sock = socket()
sock.bind(("0.0.0.0", 8090))
sock.listen(5)
# sock.setblocking(False)
sock.settimeout(3)
while True:
    try:
        print("waiting for connect...")
        connfd, addr = sock.accept()
    except BlockingIOError as e:
        time.sleep(2)
        with open("test.log", "a") as f:
            msg = "{} {}\n".format(e, time.ctime())
            f.writelines(msg)
    except timeout as e:
        with open("test.log", "a") as f:
            msg = "%s %s\n"%(e,time.ctime())
            f.write(msg)


    else:
        data = connfd.recv(1024)
