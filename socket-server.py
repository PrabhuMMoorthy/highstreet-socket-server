import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write('Hello from tornado')

class MyWebSocket(tornado.websocket.WebSocketHandler):
  clients = []

  def check_origin(self, origin):
    return True

  def open(self):
    # clients must be accessed through class object!!!
    MyWebSocket.clients.append(self)
    print("WebSocket opened")

  def on_message(self, message):
    print("msg recevied", message)
    msg = json.loads(message) # todo: safety?

    # send other clients this message
    for c in MyWebSocket.clients:
      if c != self:
        c.write_message(msg)

  def on_close(self):
    print("WebSocket closed")
    # clients must be accessed through class object!!!
    MyWebSocket.clients.remove(self)

def main():
  tornado_app = tornado.web.Application([
      (r"/", HelloHandler),
  ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  port = int(os.environ.get("PORT", 5000))
  server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
