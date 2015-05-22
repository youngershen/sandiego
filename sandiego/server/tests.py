# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com

import socket

ADDRESS = '127.0.0.1'
PORT = 8080
inet = (ADDRESS, PORT)
BUF = 1024


def index(request):
    print('index')


def test(request):
    print('test')

urls = [r'/', index]
urls += [r'/test', test]


def test_simple_tcpserver():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.connect(inet)

    while True:
        data = input('input something:\r\n')
        client.sendall(data.encode('utf8'))
        recv = client.recv(BUF)
        print(recv.decode('utf8'))

if __name__ == '__main__':
    test_simple_tcpserver()