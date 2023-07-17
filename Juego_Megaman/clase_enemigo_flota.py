import pygame
from configuraciones_animaciones import *
from clase_proyectil import Bullets

class EnemyFloat():
    def __init__(self, x, y, direccion):
        self.image = pygame.image.load('enemigo_flota\\0.png')
        self.image = pygame.transform.scale(self.image, (45,55))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direccion = direccion
        self.contador_pasos = 0
        self.move_counter = 0
        self.enemigo_derecha_flota = reescalar_imagenes(enemigo_derecha_flota, 45, 55)
        self.enemigo_izquierda_flota = reescalar_imagenes(enemigo_izquierda_flota, 45, 55)
        self.time_shot = 0
    def update(self, pantalla, lista_de_enemigos, lista_balas):
        for enemigo in lista_de_enemigos:
            enemigo.rect.y += enemigo.move_direccion
            enemigo.move_counter += 1
            if enemigo.move_direccion == 1:
                enemigo.time_shot += 50
                cooldown_shoot = 700
                enemigo.animar(pantalla, self.enemigo_derecha_flota)
                if enemigo.time_shot > cooldown_shoot:
                    enemigo.time_shot = 0
                    bullet = Bullets(enemigo.rect.right, enemigo.rect.top + 20, 1)
                    lista_balas.add(bullet)
            else:
                enemigo.time_shot += 50
                cooldown_shoot = 700
                enemigo.animar(pantalla, self.enemigo_izquierda_flota)
                if enemigo.time_shot > cooldown_shoot:
                    enemigo.time_shot = 0
                    bullet = Bullets(enemigo.rect.left, enemigo.rect.top + 20, -1)
                    lista_balas.add(bullet)
            if abs(enemigo.move_counter) > 30:
                enemigo.move_direccion *= -1
                enemigo.move_counter *= -1
    def animar(self, pantalla, lista):
        largo = len(lista)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.image = lista[self.contador_pasos]
        pantalla.blit(lista[self.contador_pasos], self.rect)
        self.contador_pasos += 1