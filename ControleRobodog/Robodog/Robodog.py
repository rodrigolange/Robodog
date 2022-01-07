import threading

import ServidorControleRobodog
import Hardware.Pernas as Pernas
import Hardware.Sonar as Sonar
from queue import Queue

filaMovimentos = Queue()


p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        print(data)
        if "-10.0" in data:
            break


print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(filaMovimentos)

t1 = threading.Thread(target=consumer, args =(filaMovimentos, ))
t1.start()