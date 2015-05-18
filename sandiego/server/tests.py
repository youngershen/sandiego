# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
import socket


def test_tcp():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # server.setblocking(False)
    server.bind(('0.0.0.0', 8080))
    server.listen(100)
    conn, addr = server.accept()
    server.shutdown(socket.SHUT_RD)

    while True:
        data = conn.recv(1024)
        if data == b'test':
            import time
            print('i am sleeping')
            time.sleep(1)
            print('down')
        else:
            print(data)

if __name__ == '__main__':
    test_tcp()
