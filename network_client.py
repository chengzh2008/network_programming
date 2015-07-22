#!usr/bin/python
__author__ = 'xiaoyazi'
"""Happy coding"""

"""before run this program, make sure to run nc in the terminal
nc -l 5555  // listening the tcp connection


// netcat is a network utility (swiss army)
// check for an open port
nc -vnz -w 1 192.168.1.9 1-30
// scan a range of port
nc -vnz -w 1 192.168.1.9 1-30
// port scanning UDP ports
nc -vnzu -w 1 192.168.1.9 50-80
// having a chat with netcat
ip a s
nc -l 2468 // one terminal
nc 127.0.0.1 2468 // the other terminal

"""


import socket

host = 'localhost'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (host, 5555)
mysock.connect(addr)

try:
    msg = b"hi, this is a test\n"
    mysock.sendall(msg)
except socket.errno as e:
    print("Socket error ", e)
finally:
    mysock.close()
