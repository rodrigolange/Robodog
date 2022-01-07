import busio
import time
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class Pernas:
    # Definicoes iniciais: endereco I2C e larguras de pulso
    def __init__(self):
        i2c = busio.I2C(SCL, SDA)
        self.pca = PCA9685(i2c, address=int('0x40', 0), reference_clock_speed=25000000)
        self.pca.frequency = 50
        self.servos = [ servo.Servo(self.pca.channels[0], min_pulse=370, max_pulse=2600),   # traseira dir lateral
                        servo.Servo(self.pca.channels[1], min_pulse=370, max_pulse=2600),   # traseira dir frente
                        servo.Servo(self.pca.channels[2], min_pulse=370, max_pulse=2600),   # traseira cotovelo
                        servo.Servo(self.pca.channels[3], min_pulse=370, max_pulse=2600),   # traseira esq lateral
                        servo.Servo(self.pca.channels[4], min_pulse=370, max_pulse=2600),   # traseira esq frente
                        servo.Servo(self.pca.channels[5], min_pulse=370, max_pulse=2600),   # traseira cotovelo
                        servo.Servo(self.pca.channels[6], min_pulse=370, max_pulse=2600),   # frente dir lateral
                        servo.Servo(self.pca.channels[7], min_pulse=370, max_pulse=2600),   # frente dir frente
                        servo.Servo(self.pca.channels[8], min_pulse=370, max_pulse=2600),   # frente dir cotovelo
                        servo.Servo(self.pca.channels[9], min_pulse=370, max_pulse=2600),   # frente esq lateral
                        servo.Servo(self.pca.channels[10], min_pulse=370, max_pulse=2600),  # frente esq frente
                        servo.Servo(self.pca.channels[11], min_pulse=370, max_pulse=2600)]  # frente esq cotovelo
        self.posicoesIniciais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]
        self.posicoesAtuais = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]
        #self.moverPosicaoInicial()
        print("Pernas init ok")

    def moverPosicaoInicial(self):
        self.moverPernasRapido(self.posicoesIniciais)

    # Movimentacao rapida dos servos
    def moverPernasRapido(self, posicoes):
        for i in range(len(posicoes)):
            self.servos[i].angle = posicoes[i]
            self.posicoesAtuais[i] = posicoes[i]
            time.sleep(0.01)

    # Movimentacao rapida dos servos - 5 graus por vez
    def moverPernasLento5(self, posicoes):
        print("inicio moverpernaslento5")
        finalizado = [True, True, True, True, True, True, True, True, True, True, True, True]
        for i in range(len(posicoes)):
            if self.posicoesAtuais[i] != posicoes[i]:
                finalizado[i] = False

        while (finalizado[0] == False or finalizado[1] == False or finalizado[2] == False or finalizado[3] == False or
            finalizado[4] == False or finalizado[5] == False or finalizado[6] == False or finalizado[7] == False or
            finalizado[8] == False or finalizado[9] == False or finalizado[10] == False or finalizado[10] == False):

            for i in range(len(posicoes)):
                if self.posicoesAtuais[i] < posicoes[i]:            # soma 5 para atingir a desejada
                    if (self.posicoesAtuais[i]+5 < posicoes[i]):
                        self.posicoesAtuais[i] +=5
                    else:
                        self.posicoesAtuais[i] = posicoes[i]
                        finalizado[i] = True
                elif self.posicoesAtuais[i] > posicoes[i]:          # subtrai 5 para atingir a desejada
                    if (self.posicoesAtuais[i]-5 > posicoes[i]):
                        self.posicoesAtuais[i] -=5
                    else:
                        self.posicoesAtuais[i] = posicoes[i]
                        finalizado[i] = True
                self.servos[i].angle = self.posicoesAtuais[i]
                time.sleep(0.01)
            #time.sleep(0.02)
        print("fim moverpernaslento5")

    # Movimentacao rapida dos servos
    def moverPernasLento10(self, posicoes):
        finalizado = [True, True, True, True, True, True, True, True, True, True, True, True]
        for i in range(len(posicoes)):
            if self.posicoesAtuais[i] != posicoes[i]:
                finalizado[i] = False

        while (finalizado[0] == False or finalizado[1] == False or finalizado[2] == False or finalizado[3] == False or
            finalizado[4] == False or finalizado[5] == False or finalizado[6] == False or finalizado[7] == False or
            finalizado[8] == False or finalizado[9] == False or finalizado[10] == False or finalizado[10] == False):

            for i in range(len(posicoes)):
                if self.posicoesAtuais[i] < posicoes[i]:            # soma 5 para atingir a desejada
                    if (self.posicoesAtuais[i]+10 < posicoes[i]):
                        self.posicoesAtuais[i]+=10
                    else:
                        self.posicoesAtuais[i] = posicoes[i]
                        finalizado[i] = True
                elif self.posicoesAtuais[i] > posicoes[i]:          # subtrai 5 para atingir a desejada
                    if (self.posicoesAtuais[i]-10 > posicoes[i]):
                        self.posicoesAtuais[i]-=10
                    else:
                        self.posicoesAtuais[i] = posicoes[i]
                        finalizado[i] = True
                self.servos[i].angle = self.posicoesAtuais[i]
                time.sleep(0.01)
            #time.sleep(0.02)

    def testeMovimentoRapido(self):
        posicoes = [90, 0, 150, 90, 180, 40, 90, 0, 150, 90, 180, 40]
        self.moverPernasRapido(posicoes)

    def testeMovimentoLento(self):
        posicoes = [90, 40, 150, 90, 140, 40, 90, 40, 150, 90, 140, 40]
        self.moverPernasLento(posicoes)
