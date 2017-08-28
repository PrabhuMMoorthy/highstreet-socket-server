import websocket
 
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://localhost:9001/")
    print("Sending 'Hello, World'...")
    ws.send('{"event": "refrestPageFromPython", "user": "TestUser", "url":"http://www.google.com"}')
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received {}".format(result))
    ws.close()
