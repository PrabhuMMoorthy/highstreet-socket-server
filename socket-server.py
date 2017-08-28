import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello from tornado')

def main():
  tornado_app = tornado.web.Application([
      ('/', HelloHandler),
  ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  port = int(os.environ.get("PORT", 5000))
  server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
