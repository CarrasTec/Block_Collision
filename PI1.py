# Creado por Crithian Carrascal
# Youtube Channel: CarrasTech

import pygame

class bloque:
    def __init__(self, x, y, ventana, masa, velocidad, tamano, color):
        self.x=x
        self.y=y
        self.ventana = ventana
        self.m = masa
        self.v = velocidad
        self.tamano = tamano
        self.color = color

    def dibujar(self):
        pygame.draw.rect(self.ventana, self.color, (self.x, self.y, self.tamano, -self.tamano))

    def mover(self):
        self.x += self.v

def refrescar(ventana):
    ventana.fill((0, 0, 0))
    b1.dibujar()
    b2.dibujar()
    text = font.render(str(golpes), True, ((255, 255, 255)))
    text_rect = text.get_rect()
    text_rect.centerx = 200
    ventana.blit(text, text_rect)


def main():
    global b1, b2, golpes, font
    ventana = pygame.display.set_mode((400, 400))
    ventana.fill((0, 0, 0))
    jugar = True
    golpes = 0
    b1 = bloque(50, 400, ventana, 1, 0, 20, (0, 255, 0))
    b2 = bloque(150, 400, ventana, 10000000000, -0.1, 50, (255, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugar = False
        refrescar(ventana)
        b1.mover()
        b2.mover()
        pygame.display.update()
        if b1.x <= 0:
            b1.v *= -1
            golpes += 1
        if b2.x <= b1.x+b1.tamano:
            v1f = ((b1.m - b2.m)/(b1.m + b2.m))*b1.v + ((2*b2.m)/(b1.m + b2.m))*b2.v
            v2f = ((2*b1.m)/(b1.m + b2.m))*b1.v + ((b2.m - b1.m)/(b1.m + b2.m))*b2.v
            b1.v = v1f
            b2.v = v2f
            golpes += 1


if __name__ == '__main__':
    main()
    pygame.quit()