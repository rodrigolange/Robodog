import ServidorControleRobodog

HOST = '127.0.0.1'
PORT = 65432

print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(HOST, PORT)

