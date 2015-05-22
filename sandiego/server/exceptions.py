# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
from sandiego.server.messages import get_http_status_message
from sandiego.server.messages import CONNECTION_CLOSED_EXCEPTION


class BaseHttpException(Exception):

    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        if self.message:
            message = get_http_status_message(self.code) + "\r\n" + self.message
        else:
            message = get_http_status_message(self.code)

        return get_http_status_message(message)


class HttpException(BaseHttpException):
    pass


class ConnectionClosedException(Exception):

    def __str__(self):
        return CONNECTION_CLOSED_EXCEPTION

