import threading
import socket

HOST = '0.0.0.0'
PORT = 65432

class ServidorControleRobodog:

    def socketServidor(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("criando socket")
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    listaPosicoes = data.decode().split(",")
                    self.filaMovimentos.put(listaPosicoes)

                    if "-10.0" in data.decode():
                        break




    def __init__(self, filaMovimentos):

        self.filaMovimentos = filaMovimentos

        print("Criando servidor socket")
        x = threading.Thread(target=self.socketServidor)
        print("Iniciando servidor socket")
        x.start()
