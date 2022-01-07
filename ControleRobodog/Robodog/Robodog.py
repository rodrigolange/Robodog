import ServidorControleRobodog
import Hardware.Pernas as Pernas
import Hardware.Sonar as Sonar

p = Pernas.Pernas()
s = Sonar.Sonar(23, 24)


print("Iniciando servidor de controle do Robodog")
Robodog = ServidorControleRobodog.ServidorControleRobodog()

