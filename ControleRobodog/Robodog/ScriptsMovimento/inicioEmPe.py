import time
import Pernas
import Sonar
posicoesF = [80, 0, 150, 100, 180, 40, 80, 50, 120, 100, 130, 70]  # levanta frente
posicoesT = [80, 30, 120, 100, 150, 70, 80, 50, 120, 100, 130, 70]  # levanta atras
posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)

time.sleep(1)

p.moverPernasLento10(posicoesF) # levanta pernas da frente
time.sleep(0.5)
p.moverPernasLento10(posicoesT) # levanta pernas traseiras
time.sleep(1)

