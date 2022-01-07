import ServidorControleRobodog

HOST = '0.0.0.0'
PORT = 65432

print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(HOST, PORT)

