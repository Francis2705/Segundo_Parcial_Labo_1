import pygame

class Health():
    def __init__(self, x, y, ancho, largo, movimiento):
        self.image = pygame.image.load('objetos\\vida_total.png')
        self.image = pygame.transform.scale(self.image, (ancho,largo))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movimiento = movimiento
        self.counter = 1
    def update(self, pantalla, lista_de_vidas):
        for vida in lista_de_vidas:
            pantalla.blit(vida.image, vida.rect)
            if abs(vida.counter) < 10:
                vida.rect.y += vida.movimiento
                vida.counter += 1
            else:
                vida.counter *= -1
                vida.counter += 1
                vida.movimiento *= -1