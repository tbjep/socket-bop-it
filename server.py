from socketserver import BaseRequestHandler, DatagramRequestHandler, UDPServer

class MyHandler(DatagramRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        print(data)
        print(socket)
        socket.sendto(data.upper(), self.client_address)

def main():
    with UDPServer(('127.0.0.1', 3333), MyHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()
