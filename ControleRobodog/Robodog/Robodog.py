# dados[0] = stick esquerda, lateral
# dados[1] = stick esquerda, frente
# dados[2] = stick direita, lateral
# dados[3] = stick direita, frente


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

        print(dados)

        if dados[4] == 10 and dados[10] == 0:
            if 0 < posicoesPernas[10] + int(dados[1]) < 180:
                print("nova posicao pernas[10]")
                posicoesPernas[10] = posicoesPernas[10] + int(dados[1])
                print(posicoesPernas[10])

        if dados[5] == 10 and dados[11] == 0:
            if 0 < posicoesPernas[7] + int(dados[3]) < 180:
                print("nova posicao pernas[7]")
                posicoesPernas[7] = posicoesPernas[7] + int(dados[3])
                print(posicoesPernas[7])

        if dados[6] == 10 and dados[10] == 0:
            if 0 < posicoesPernas[11] + int(dados[3]) < 180:
                print("nova posicao pernas[11]")
                posicoesPernas[11] = posicoesPernas[11] + int(dados[3])
                print(posicoesPernas[11])


        p.moverPernasRapido(posicoesPernas)







print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(filaMovimentos)

tMovimentoRobodog = threading.Thread(target=movimentoRobodog, args =(filaMovimentos, ))
tMovimentoRobodog.start()
