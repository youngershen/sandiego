# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com


class HTTPBASERequest:
    METHOD = None
    META = None
    ENVIRON = None
    GET = None
    POST = None
    PATH = None
    PATH_INFO = None
    HANDLER = None


class HTTPRequest(HTTPBASERequest):

    def __init__(self, method=None, meta=None, environ=None, path=None, path_info=None, handler=None):
        self.METHOD = method
        self.META = meta
        self.ENVIRON = environ
        self.PATH = path
        self.PATH_INFO = path_info
        self.HANDLER = handler
        self.GET = dict()
        self.POST = dict()

    def __getattribute__(self, item):
        if 'GET' == item:
            pass

        if 'POST' == item:
            pass