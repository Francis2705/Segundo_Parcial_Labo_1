import pygame
from configuraciones_animaciones import *
from clase_proyectil import Bullets
from clase_proyectil_boss import BulletsBoss

class BossFinal():
    def __init__(self, x, y, direccion):
        self.image = pygame.image.load('chatgpt\\0.png')
        self.image = pygame.transform.scale(self.image, (75,95))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direccion = direccion
        self.contador_pasos = 0
        self.move_counter = 0
        self.time_shot = 0
        self.boss_final = reescalar_imagenes(boss_final, 75, 95)
        self.health_start = 50
        self.health_remaining = 50
        self.time_shot_especial = 0
    def update(self, pantalla, lista_de_enemigos, lista_balas, player, lista_balas_boss):
        for enemigo in lista_de_enemigos:
            rectangulo_vida_roja = pygame.Rect(200,80,600,20) #barra de vida
            pygame.draw.rect(pantalla, 'Red', rectangulo_vida_roja)
            if enemigo.health_remaining > 0: #significa que todavia esta con vida
                rectangulo_vida_verde = pygame.Rect(200, 80, int(rectangulo_vida_roja.width * (enemigo.health_remaining / enemigo.health_start)), 20)
                pygame.draw.rect(pantalla, 'Green', rectangulo_vida_verde)
            else:
                player.game_over = 1
            enemigo.animar(pantalla, self.boss_final)
            enemigo.rect.y += enemigo.move_direccion
            enemigo.rect.x += enemigo.move_direccion *-1
            enemigo.move_counter += 1
            enemigo.time_shot += 50
            cooldown_shoot = 900
            if enemigo.time_shot > cooldown_shoot:
                enemigo.time_shot = 0
                bullet = Bullets(enemigo.rect.left, enemigo.rect.top + 45, -1)
                lista_balas.add(bullet)

            enemigo.time_shot_especial += 50
            cooldown_shoot_especial = 4000
            if enemigo.time_shot_especial > cooldown_shoot_especial:
                enemigo.time_shot_especial = 0
                bullet_boss = BulletsBoss(enemigo.rect.left, enemigo.rect.top + 45, -1)
                lista_balas_boss.add(bullet_boss)
            if abs(enemigo.move_counter) > 200:
                enemigo.move_direccion *= -1
                enemigo.move_counter *= -1
    def animar(self, pantalla, lista):
        largo = len(lista)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.image = lista[self.contador_pasos]
        pantalla.blit(lista[self.contador_pasos], self.rect)
        self.contador_pasos += 1