import time
import Pernas
import Sonar
posicoesF = [80, 0, 150, 100, 180, 40, 80, 50, 120, 100, 130, 70]  # levanta frente
posicoesT = [80, 30, 120, 100, 150, 70, 80, 50, 120, 100, 130, 70]  # levanta atras


posicoes = [[80, 30, 150, 100, 150, 70, 80, 50, 120, 100, 130, 70],  # avanca perna traseira direita
            [80, 80, 150, 100, 150, 70, 80, 50, 120, 100, 130, 70]]

posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)


p.moverPernasLento5(posicoesF) # levanta pernas da frente - 5 = 5ms entre avanco de graus
time.sleep(0.1)
p.moverPernasLento5(posicoesT) # levanta pernas traseiras
time.sleep(0.5)


for _ in range(10):
     for i in range(len(posicoes)):
          p.moverPernasRapido(posicoes[i])
          time.sleep(0.25)
     time.sleep(0.5)

p.moverPernasLento5(posicoesF)
time.sleep(0.1)
p.moverPernasLento5(posicoesT)
time.sleep(0.5)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)
