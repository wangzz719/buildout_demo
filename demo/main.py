#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 11:54
# @Author  : wangzz
# @File    : main.py

import tornado.httpserver
import tornado.wsgi
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=12316, help="run on the given port", type=int)

from demo.hello_word import MainHandler

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/hello", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
