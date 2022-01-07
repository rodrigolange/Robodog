import threading
import time

import ServidorControleRobodog
import Hardware.Pernas as Pernas
import Hardware.Sonar as Sonar
from queue import Queue

filaMovimentos = Queue()


p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]
posicoesF = [80, 0, 150, 100, 180, 40, 80, 50, 120, 100, 130, 70]  # levanta frente
posicoesPernas = posicoesF


def movimentoRobodog(in_q):

    p.moverPernasLento10(posicoesIniciais)
    time.sleep(1)

    p.moverPernasLento10(posicoesPernas)
    time.sleep(1)

    while True:
        data = in_q.get()
        if "-10.0" in data:
            break

        dados = [float(x)*10 for x in data]

        if posicoesPernas[10] + int(dados[10]) > 0 and posicoesPernas[10] + int(dados[10]) < 200:
            posicoesPernas[10] = posicoesPernas[10] + int(dados[1])
            p.moverPernas(posicoesPernas)
            print(posicoesPernas[10])









print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(filaMovimentos)

tMovimentoRobodog = threading.Thread(target=movimentoRobodog, args =(filaMovimentos, ))
tMovimentoRobodog.start()
