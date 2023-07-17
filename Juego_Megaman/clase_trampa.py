import pygame
from configuraciones_animaciones import *

class Tramp():
    def __init__(self, x, y, movimiento):
        self.image = pygame.image.load('objetos\\trampa1.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_pasos = 0
        self.move_direccion = movimiento
        self.move_counter = 0
        self.trampas_giratorias = reescalar_imagenes(trampa_sierra, 30, 30)
    def update(self, pantalla, lista_de_trampas):
        for trampa in lista_de_trampas:
            trampa.animar(pantalla, self.trampas_giratorias)
            trampa.rect.x += trampa.move_direccion
            trampa.move_counter += 1
            if abs(trampa.move_counter) > 20:
                trampa.move_direccion *= -1
                trampa.move_counter *= -1
    def animar(self, pantalla, lista):
        largo = len(lista)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.image = lista[self.contador_pasos]
        pantalla.blit(lista[self.contador_pasos], self.rect)
        self.contador_pasos += 1