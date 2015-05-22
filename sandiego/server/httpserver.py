# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
from .tcpserver import TCPBASEServer


class HTTPBASEServer(TCPBASEServer):
    @staticmethod
    def handler(connection):
        pass


class HTTPServer(HTTPBASEServer):
    pass