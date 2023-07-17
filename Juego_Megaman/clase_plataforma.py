import pygame

class Platform():
    def __init__(self, x, y, ancho, largo):
        self.image = pygame.image.load('objetos\plataforma.png')
        self.image = pygame.transform.scale(self.image, (ancho,largo))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pared1 = pygame.Rect(self.rect.x, self.rect.y -50, 2, 50)
        self.pared2 = pygame.Rect(self.rect.x + self.rect.width - 2, self.rect.y -50, 2, 50)
    def update(self, pantalla, lista_de_plataformas):
        for plataforma in lista_de_plataformas:
            pantalla.blit(plataforma.image, plataforma.rect)