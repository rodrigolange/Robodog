import time
import Hardware.Pernas as Pernas
import Hardware.Sonar as Sonar
posicoesF = [80, 0, 150, 100, 180, 40, 80, 50, 120, 100, 130, 70]  # levanta frente
posicoesT = [80, 30, 120, 100, 150, 70, 80, 50, 120, 100, 130, 70]  # levanta atras


posicoesEFD1 = [80, 30, 150, 100, 150, 70, 80, 50, 120, 100, 130, 70]  # avanca perna traseira direita
posicoesEFD2 = [80, 80, 150, 100, 150, 70, 80, 50, 120, 100, 130, 70]
posicoesEFD3 = [80, 80, 120, 100, 150, 70, 80, 50, 120, 100, 130, 70]

posicoesEFD4 = [80, 80, 120, 100, 160, 70, 80, 50, 120, 100, 130, 70]  # avanca traseira esquerda
posicoesEFD5 = [80, 80, 120, 100, 160, 40, 80, 50, 120, 100, 130, 70]
posicoesEFD6 = [80, 80, 120, 100, 130, 40, 80, 50, 120, 100, 130, 70]

posicoesEFD7 = [80, 80, 120, 100, 130, 40, 80, 100, 100, 100, 130, 70]  #avanca perna frente direita

posicoesEFD8 = [80, 50, 120, 100, 130, 40, 80, 100, 100, 100, 130, 70] # sobe perna traseira direita

posicoesEFD9 = [80, 50, 120, 100, 130, 70, 80, 100, 100, 100, 130, 70] # sobe perna traseira esquerda

posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)

p.moverPernasLento10(posicoesF) # levanta pernas da frente
time.sleep(0.5)
p.moverPernasLento10(posicoesT) # levanta pernas traseiras
time.sleep(1)

#p.moverPernasLento5(posicoesE)  # move quadril para direita
#time.sleep(1)



p.moverPernasRapido(posicoesEFD1)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD2)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD3)
time.sleep(0.5)


p.moverPernasRapido(posicoesEFD4)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD5)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD6)
time.sleep(0.5)


p.moverPernasRapido(posicoesEFD7)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD8)
time.sleep(0.5)

p.moverPernasRapido(posicoesEFD9)
time.sleep(0.5)

print("Distancia: ", s.getDistancia(), " cm")
time.sleep(1)
