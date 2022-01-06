import socket


class Cliente:

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def enviar(self, valor):
        if valor == -10:
            self.s.close()
        else:
            self.s.sendall(str(valor).encode('utf-8'))