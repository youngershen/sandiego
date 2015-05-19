# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com

import tornado.ioloop
import tornado.web


def start_server(port, address=""):
    application = tornado.web.Application([])
    application.listen(port, address)
    tornado.ioloop.IOLoop.instance().start()