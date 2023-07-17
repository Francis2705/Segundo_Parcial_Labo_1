import pygame
from configuraciones_animaciones import *

class Enemy():
    def __init__(self, x, y):
        self.image = pygame.image.load('enemigo\\0.png')
        self.image = pygame.transform.scale(self.image, (45,55))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direccion = 1
        self.contador_pasos = 0
        self.enemigo_derecha = reescalar_imagenes(enemigo_derecha, 45, 55)
        self.enemigo_izquierda = reescalar_imagenes(enemigo_izquierda, 45, 55)
    def update(self, pantalla, lista_de_enemigos, lista_de_plataformas):
        for enemigo in lista_de_enemigos:
            enemigo.rect.x += enemigo.move_direccion
            for i in range(len(lista_de_plataformas)): #colisionar con paredes
                if enemigo.move_direccion == 1:
                    enemigo.animar(pantalla, self.enemigo_derecha)
                else:
                    enemigo.animar(pantalla, self.enemigo_izquierda)
                if enemigo.rect.colliderect(lista_de_plataformas[i].pared2):
                    enemigo.move_direccion *= -1
                if enemigo.rect.colliderect(lista_de_plataformas[i].pared1):
                    enemigo.move_direccion *= -1
    def animar(self, pantalla, lista):
        largo = len(lista)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.image = lista[self.contador_pasos]
        pantalla.blit(lista[self.contador_pasos], self.rect)
        self.contador_pasos += 1