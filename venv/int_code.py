import sockets

class Lambda_Sockets:

    host_ip = '127.0.0.1'
    host_port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @staticmethod
    def init():
        s.bind((host_ip, port_ip))

    @staticmethod
    def listen():
        s.listen()
        conn, addr = s.accept()

    @staticmethod
    def connect(host, port):
        s.connect((host, port))

    @staticmethod
    def disconnect():
        s.close()

    @staticmethod
    def send(data):
        s.sendall(data.encode())

    @staticmethod
    def receive():
        message = conn.recv(1024)
        print(message.decode())

