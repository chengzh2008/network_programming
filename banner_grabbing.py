#!usr/bin/python
__author__ = 'xiaoyazi'
"""Happy coding"""

import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.microsoft.com', 80))

http_get = b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data = ''
try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
except socket.error:
    print('Socket error', socket.errno)
finally:
    print('closing connection')
    sock.close()

strdata = data[0].decode('utf-8')
headers = strdata.splitlines()

for s in headers:
    print s
    if re.search('Server:', s):
        s = s.replace('Server: ', "")
        print(s)