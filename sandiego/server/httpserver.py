# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
import socket
from sandiego.server.tcpserver import TCPBASEServer
from sandiego.server.exceptions import ConnectionClosedException
RECV_BUF = 1024
HTTPHEADER = b"HTTP/1.1 200 Ok \r\n"


class HTTPBASEServer(TCPBASEServer):
    def handler(self, connection):
        raise NotImplementedError()

    @staticmethod
    def parse_header(data):
        data = data.decode('utf8')
        return data

    @staticmethod
    def build_header(header=None, data=None, d=False):
        if not header:
            header = HTTPHEADER

        if data:
            for i in range(len(data.items())):
                key, value = data.popitem()
                header_str = bytearray(key, 'ascii') + b':' + bytearray(value, 'ascii') + b'\r\n'
                header += header_str
        if d:
            header += b'\r\n'

        return header

    @staticmethod
    def build_response(header=None, content=None):
        if content:
            content = content.encode('utf8')
        else:
            content = b''
        header = header + b'\r\n' + content
        return header


class HTTPServer(HTTPBASEServer):
    def handler(self, connection):
        recv = connection.recv(1024)
        print(recv)

        headers = {'Connection': 'close', 'Content-Length': '12', 'Content-Type': 'text/html; charset=utf-8',
        body = 'best server'
        body_length = len(body)

        header = self.build_header(data=headers)
        response = self.build_response(header, 'youngers server')

        try:
            connection.send(response)
            connection.sendall(response)
        except socket.error:
            raise ConnectionClosedException()
