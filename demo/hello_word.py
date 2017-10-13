#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/13 11:56
# @Author  : wangzz
# @File    : hello_word.py

import time

import tornado.web




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Connection', 'keep-alive')
        self.write("Hello, world {} | {}".format(self.request.path, int(time.time())))




