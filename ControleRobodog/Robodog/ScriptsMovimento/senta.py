import time
import Pernas
import Sonar
posicoes = [90, 60, 150, 90, 120, 40, 90, 60, 150, 90, 120, 40]
posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)
#p.moverPosicaoInicial()

for x in range(0, 1):
	time.sleep(2)
	p.moverPernasLento5(posicoes)
	print("Distancia: ", s.getDistancia(), " cm")
	time.sleep(2)
	p.moverPernasLento5(posicoesIniciais)
	print("Distancia: ", s.getDistancia(), " cm")

for x in range(0, 1):
        time.sleep(2)
        p.moverPernasLento10(posicoes)
        print("Distancia: ", s.getDistancia(), " cm")
        time.sleep(2)
        p.moverPernasLento10(posicoesIniciais)
        print("Distancia: ", s.getDistancia(), " cm")
        time.sleep(2)
        p.moverPernasLento10(posicoes)
        print("Distancia: ", s.getDistancia(), " cm")
