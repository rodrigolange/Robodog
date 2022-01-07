import pygame

import Cliente

#ip robodog: 10.0.0.200
HOST = '10.0.0.200'
PORT = 65432

BLACK = pygame.Color('black')
BLUE = pygame.Color('blue')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
WHITE = pygame.Color('white')


class TextPrint(object):

    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((640, 380))
pygame.display.set_caption("RoboDog GUI")


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates.
clock = pygame.time.Clock()
# Initialize the joysticks.
pygame.joystick.init()
# Get ready to print.
nroBotoesJoystick = pygame.joystick.Joystick(0).get_numbuttons()

print("nro botoes: " + str(nroBotoesJoystick))

#servidor = ServidorControleRobodog.ServidorControleRobodog('10.0.0.200', PORT)
cliente = Cliente.Cliente(HOST, PORT)
textPrint = TextPrint()

joystick = pygame.joystick.Joystick(0)
joystick.init()

v = [0.0, 0.0, 0.0, 0.0]
botoes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dados = "0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,"
dadosZero = "0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,0.0"
#dadosAnterior = "0.0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0,0,0,0,"

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cliente.enviar("-10.0,-10.0,-10.0")
            done = True

    if done == True:
        break

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (300, 50, 50, 50))
    pygame.draw.rect(screen, BLACK, (400, 50, 50, 50))
    pygame.draw.rect(screen, BLACK, (300, 150, 50, 50))
    pygame.draw.rect(screen, BLACK, (400, 150, 50, 50))

    textPrint.reset()
    textPrint.indent()

    dados = ''

    for axis in range(0, 4):
        v[axis] = joystick.get_axis(axis)
        textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(axis, v[axis]))
        dados = dados + str(v[axis]) + ","

    for botao in range(0, nroBotoesJoystick):
        botoes[botao] = pygame.joystick.Joystick(0).get_button(botao)
        dados = dados + str(botoes[botao]) + ","
        textPrint.tprint(screen, "Botao {} value: {}".format(botao, botoes[botao]))

    dados = dados + "0.0"
    if dados != dadosZero:
        cliente.enviar(dados)

    if botoes[4] == 1 and botoes[10] == 0:
        pygame.draw.rect(screen, (255, 0, 0), (300, 50, 50, 50))
    if botoes[4] == 1 and botoes[10] == 1:
        pygame.draw.rect(screen, (255, 0, 0), (300, 50, 50, 50))
        pygame.draw.rect(screen, (0, 0, 0), (310, 60, 30, 30))

    if botoes[5] == 1 and botoes[11] == 0:
        pygame.draw.rect(screen, (0, 255, 0), (400, 50, 50, 50))
    if botoes[5] == 1 and botoes[11] == 1:
        pygame.draw.rect(screen, (0, 255, 0), (400, 50, 50, 50))
        pygame.draw.rect(screen, (0, 0, 0), (410, 60, 30, 30))

    if botoes[6] == 1 and botoes[10] == 0:
        pygame.draw.rect(screen, (0, 0, 255), (300, 150, 50, 50))
    if botoes[6] == 1 and botoes[10] == 1:
        pygame.draw.rect(screen, (0, 0, 255), (300, 150, 50, 50))
        pygame.draw.rect(screen, (0, 0, 0), (310, 160, 30, 30))

    if botoes[7] == 1 and botoes[11] == 0:
        pygame.draw.rect(screen, (255, 255, 0), (400, 150, 50, 50))
    if botoes[7] == 1 and botoes[11] == 1:
        pygame.draw.rect(screen, (255, 255, 0), (400, 150, 50, 50))
        pygame.draw.rect(screen, (0, 0, 0), (410, 160, 30, 30))

    pygame.display.flip()
    # Limit to 2 frames per second.
    clock.tick(5)
pygame.quit()
