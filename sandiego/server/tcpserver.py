# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
import sys
import socket
import threading
from sandiego.server.exceptions import ConnectionClosedException


class TCPBASEThread(threading.Thread):
    pass


class TCPThread(TCPBASEThread):

    def __init__(self, handler, connection, address):
        super().__init__()
        self.handler = handler
        self.connection = connection
        self.address = address

    def run(self):
        while True:
            try:
                self.handler(self.connection)
            except ConnectionClosedException:
                print('connection closed')
                sys.exit(0)


class TCPBASEServer:

    def __init__(self, address='127.0.0.1', port=8080, listen=128):
        self.address = address
        self.port = port
        self.listen = listen
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((address, port))
        self.socket.listen(self.listen)

    def serve(self):
        while True:
            try:
                connection, address = self.socket.accept()
            except socket.error as e:
                print(e)
            else:
                self.process(connection, address)

    def process(self, connection, address):
        processing = TCPThread(self.handler, connection, address)
        processing.start()

    def handler(self, connection):
        raise NotImplementedError()


class TCPServer(TCPBASEServer):
    def handler(self, connection):
        data = connection.recv(1024)
        print(data)
        connection.sendall(data)


if __name__ == '__main__':
    server = TCPServer()
    server.serve()
