import socket

def main():
    server_addr = ('127.0.0.1', 3333)
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.sendto(b"hello", server_addr)
    data = sock.recv(1024)
    print(data)

if __name__ == "__main__":
    main()
