import time
import Pernas
import Sonar

delayMovimentos = 3.05
delayCiclos = 3.05

#80, 100
posicoesF = [90, 0, 150, 90, 180, 40, 90, 50, 120, 90, 130, 70]  # levanta frente
posicoesT = [90, 45, 120, 90, 135, 70, 90, 50, 120, 90, 130, 70]  # levanta atras


posicoes = [[90, 45, 130, 90, 135, 70, 90, 50, 120, 90, 130, 60],  # sobe perna traseira direita e frente esq
            [90, 45, 130, 90, 135, 80, 90, 50, 110, 90, 130, 60],  # avanca cotovelo traseiro esq e frente dir
            [90, 45, 120, 90, 135, 90, 90, 50, 100, 90, 130, 75]]  # baixa perna tras. dir e frente esq

posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)


p.moverPernasLento5(posicoesF) # levanta pernas da frente - 5 = 5ms entre avanco de graus
time.sleep(0.1)
p.moverPernasLento5(posicoesT) # levanta pernas traseiras
time.sleep(0.5)

time.sleep(1)

for _ in range(5):
     for i in range(len(posicoes)):
          p.moverPernasRapido(posicoes[i])
          time.sleep(delayMovimentos)
     time.sleep(delayCiclos)

#p.moverPernasLento5(posicoesF)
#time.sleep(0.1)

p.moverPernasRapido(posicoesT)
time.sleep(0.5)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)
