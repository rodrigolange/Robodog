import threading
import socket


class ServidorControleRobodog:

    def socketServidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data or data.decode() == -10:
                        break
                    print(data.decode())

    def __init__(self, host, port):

        self.HOST = host
        self.PORT = port

        x = threading.Thread(target=self.socketServidor)
        x.start()
