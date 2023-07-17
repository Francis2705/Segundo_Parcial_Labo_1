import pygame

class Coin():
    def __init__(self, x, y, ancho, largo, movimiento):
        self.image = pygame.image.load('objetos\coin.png')
        self.image = pygame.transform.scale(self.image, (ancho,largo))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movimiento = movimiento
        self.counter = 1
    def update(self, pantalla, lista_de_monedas):
        for moneda in lista_de_monedas:
            pantalla.blit(moneda.image, moneda.rect)
            if abs(moneda.counter) < 10:
                moneda.rect.y += moneda.movimiento
                moneda.counter += 1
            else:
                moneda.counter *= -1
                moneda.counter += 1
                moneda.movimiento *= -1