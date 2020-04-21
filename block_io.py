"""
block_io.py 非阻塞io演示
"""
from socket import *
from time import ctime,sleep

f = open('log.txt','a') # 日志文件

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

# 设置套接字非阻塞
# s.setblocking(False)

# 设置超时时间
s.settimeout(3)

while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except (BlockingIOError,timeout) as e:
        sleep(2)
        f.write(ctime()+':'+str(e)+'\n')
    else:
        data = c.recv(1024)
        print(data)




