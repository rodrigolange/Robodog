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

def movimentoRobodog(in_q):
    posInicial = [80, 0, 150, 100, 180, 40, 80, 50, 120, 100, 130, 70]  # levanta frente
    posicoesPernas = posInicial

    p.moverPernasLento10(posicoesPernas)
    time.sleep(1)

    while True:
        data = in_q.get()
        if "-10.0" in data:
            break

        dados = [float(x)*10 for x in data]

        if dados[5] == 10:
            print("dados[5]")
            posicoesPernas = posInicial
        else:
            if dados[8] == 10 and dados[14] == 0:
                if 0 < posicoesPernas[10] + int(dados[1]) < 180:
                    #print("nova posicao pernas[10]: " + str(posicoesPernas[10]))
                    posicoesPernas[10] = posicoesPernas[10] + int(dados[1])

            if dados[9] == 10 and dados[15] == 0:
                if 0 < posicoesPernas[7] - int(dados[3]) < 180:
                    #print("nova posicao pernas[7]")
                    posicoesPernas[7] = posicoesPernas[7] - int(dados[3])

            if dados[10] == 10 and dados[14] == 0:
                if 0 < posicoesPernas[11] + int(dados[1]) < 180:
                    #print("nova posicao pernas[11]")
                    posicoesPernas[11] = posicoesPernas[11] + int(dados[1])

            if dados[11] == 10 and dados[15] == 0:
                if 0 < posicoesPernas[8] - int(dados[3]) < 180:
                    #print("nova posicao pernas[8]")
                    posicoesPernas[8] = posicoesPernas[8] - int(dados[3])

        p.moverPernasRapido(posicoesPernas)


print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog(filaMovimentos)

tMovimentoRobodog = threading.Thread(target=movimentoRobodog, args=(filaMovimentos,))
tMovimentoRobodog.start()
