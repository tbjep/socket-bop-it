from socketserver import UDPServer, BaseRequestHandler

class MyHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request[0]
        print(self.data)

def main():
    with UDPServer(('127.0.0.1', 3333), MyHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()
