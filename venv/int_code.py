import socket

class Lambda_Sockets:

    def __init__(self):
        self.host_ip = '127.0.0.1'
        self.host_port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = 0
        self.addr = 0

    def init(self):
        self.s.bind((self.host_ip, self.host_port))

    def listen(self):
        self.s.listen()
        self.conn, self.addr = self.s.accept()

    def connect(self, host, port):
        self.s.connect((host, port))

    def disconnect(self):
        self.s.close()

    def client_send(self, data):
        self.s.sendall(data.encode())

    def server_send(self, data):
        self.conn.sendall(data.encode())

    def server_receive(self):
        message = self.conn.recv(1024)
        print(message.decode())
    
    def client_receive(self):
        message = self.s.recv(1024)
        print(message.decode())

