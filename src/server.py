#!/usr/bin/env python

import threading
import logging
import time

import serial
import tornado.web

from data import Session, Reading
import settings
from tornado import httpserver
from api import URLS

log = logging.getLogger()

def standalone():
    io_loop = tornado.ioloop.IOLoop.instance()

    app_settings = {
        "gzip": True,
        "cookie_secret": 'uyG9hklV8k4Epx5D5HwoYXP7YDnyVFtJ755xqpNKno7LZFe4jx0',
        "debug": settings.TORNADO_DEBUG,
    }
    application = tornado.web.Application(URLS, **app_settings)

    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)

    io_loop.start()

if __name__ == '__main__':
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
    handler = logging.FileHandler("/tmp/sensor-log-server.log")
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    log.info("Starting up")
    standalone()
