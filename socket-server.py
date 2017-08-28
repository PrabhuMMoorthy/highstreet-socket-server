#!/usr/bin/env python

from tornado.options import options, define, parse_command_line
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket
import json

define('port', type=int, default=9001)

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello from tornado')

def main():
  tornado_app = tornado.web.Application([
      ('/', HelloHandler),
      ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
