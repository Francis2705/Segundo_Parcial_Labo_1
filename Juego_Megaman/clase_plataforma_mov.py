import pygame
from clase_plataforma import Platform

class PlatformMoving(Platform):
    def __init__(self, x, y, ancho, largo, movimiento):
        super().__init__(x, y, ancho, largo)
        self.movimiento = movimiento
        self.counter = 1
        self.pared_colision_personaje1 = pygame.Rect(self.rect.x, self.rect.y + 2, 2, largo - 5)
        self.pared_colision_personaje2 = pygame.Rect(self.rect.x + self.rect.width, self.rect.y + 2, 2, largo - 5)

    def update(self, pantalla, lista_de_plataformas_moviendose): #lo hago devuelta porque le agrego el movimiento y le paso otra lista
        for plataforma in lista_de_plataformas_moviendose:
            pantalla.blit(plataforma.image, plataforma.rect)
            if abs(plataforma.counter) < 60:
                plataforma.rect.y += plataforma.movimiento
                plataforma.pared_colision_personaje1.y += plataforma.movimiento
                plataforma.pared_colision_personaje2.y += plataforma.movimiento
                plataforma.counter += 1
            else:
                plataforma.counter *= -1
                plataforma.counter += 1
                plataforma.movimiento *= -1