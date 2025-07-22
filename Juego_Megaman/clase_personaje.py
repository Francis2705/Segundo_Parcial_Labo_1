import pygame
from clase_proyectil import Bullets
from configuraciones_animaciones import *

class Player():
    def __init__(self, x, y, vida):
        try:
            self.reset(x, y, vida)
        except AttributeError as e:
            with open('errores.txt','a') as error:
                error.write(f'Error -> "{e}"\n')
    def update(self, pantalla, lista_plataformas, lista_de_trampas, lista_de_enemigos, lista_de_monedas, lista_plataformas_movimiento,
            lista_balas, lista_vidas, lista_enemigos_flotantes, rectangulo_final, flag_sonidos_colision):
        rectangulo_vida_roja = pygame.Rect(200,40,500,20) #barra de vida
        pygame.draw.rect(pantalla, 'Red', rectangulo_vida_roja)
        if self.health_remaining > 0: #significa que todavia esta con vida
            rectangulo_vida_verde = pygame.Rect(200, 40, int(rectangulo_vida_roja.width * (self.health_remaining / self.health_start)), 20)
            pygame.draw.rect(pantalla, 'Green', rectangulo_vida_verde)
        else: #murio por vida
            self.game_over = -1
        dx = 0 #coordenada en la q se mueve en x
        dy = 0 #coordenada en la q se mueve en y
        if self.game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_UP] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                if self.rect.left > 0:
                    if self.in_air == False:
                        self.animar(pantalla, self.personaje_izquierda_camina)
                    self.flag_derecha = False
                    dx -= 10
                else:
                    if self.in_air == False:
                        self.animar(pantalla, self.personaje_izquierda_camina)
                    self.flag_derecha = False
            if key[pygame.K_RIGHT]:
                if self.rect.right < 1195:
                    if self.in_air == False:
                        self.animar(pantalla, self.personaje_derecha_camina)
                    self.flag_derecha = True
                    dx += 10
                else:
                    if self.in_air == False:
                        self.animar(pantalla, self.personaje_derecha_camina)
                    self.flag_derecha = True
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_z] == False:
                if self.in_air == False:
                    if self.flag_derecha == True:
                        self.animar(pantalla, self.personaje_derecha_quieto)
                    else:
                        self.animar(pantalla, self.personaje_izquierda_quieto)
            if self.in_air == True:
                if self.flag_derecha == True:
                    self.animar(pantalla, self.personaje_derecha_salta)
                else:
                    self.animar(pantalla, self.personaje_izquierda_salta)
            if key[pygame.K_z] and self.in_air == False:
                self.esta_pegando = True
                if self.flag_derecha == True:
                    self.animar(pantalla, self.personaje_derecha_mele)
                else:
                    self.animar(pantalla, self.personaje_izquierda_mele)
            if key[pygame.K_z] == False:
                self.esta_pegando = False
            #Disparo y cooldown para el disparo
            self.time_shot += 50
            cooldown_shoot = 500
            if key[pygame.K_SPACE] and self.time_shot > cooldown_shoot: #
                if self.flag_derecha == True:
                    self.animar(pantalla, personaje_dispara_derecha)
                    self.time_shot = 0
                    bullet = Bullets(self.rect.right, self.rect.top + 20, 1)
                    lista_balas.add(bullet)
                else:
                    self.animar(pantalla, personaje_dispara_izquierda)
                    self.time_shot = 0
                    bullet = Bullets(self.rect.left, self.rect.top + 20, -1)
                    lista_balas.add(bullet)
            #Gravedad
            self.vel_y += 1
            if self.vel_y > 10: #esto es la gravedad con la que caigo
                self.vel_y = 10
            dy += self.vel_y
            self.in_air = True #esto va a ser True si y solo si, no esta colisionando con una plataforma y no esta cayendo contra una

            for i in range(len(lista_plataformas)): #verificar si colisiono con plataformas y rectangulo final
                otro_rectangulo_futuro_x = pygame.Rect(self.rect.x + dx, self.rect.y, self.width, self.height)
                if otro_rectangulo_futuro_x.colliderect(lista_plataformas[i].rect) or otro_rectangulo_futuro_x.colliderect(rectangulo_final):
                    dx = 0
                otro_rectangulo_futuro_y = pygame.Rect(self.rect.x, self.rect.y + dy, self.width, self.height)
                if otro_rectangulo_futuro_y.colliderect(lista_plataformas[i].rect): #collision in y
                    if self.vel_y < 0: #si esta saltando
                        dy = lista_plataformas[i].rect.bottom - self.rect.top
                    elif self.vel_y >= 0: #si esta cayendo
                        dy = lista_plataformas[i].rect.top - self.rect.bottom
                        self.in_air = False
                    self.vel_y = 0
            for i in range(len(lista_plataformas_movimiento)): #verificar si colisiono con plataformas en movimiento
                otro_rectangulo_futuro_x = pygame.Rect(self.rect.x + dx, self.rect.y, self.width, self.height)
                if (otro_rectangulo_futuro_x.colliderect(lista_plataformas_movimiento[i].pared_colision_personaje1) or 
                    otro_rectangulo_futuro_x.colliderect(lista_plataformas_movimiento[i].pared_colision_personaje2)): #collision in x
                    dx = 0
                otro_rectangulo_futuro_y = pygame.Rect(self.rect.x, self.rect.y + dy, self.width, self.height)
                if otro_rectangulo_futuro_y.colliderect(lista_plataformas_movimiento[i].rect): #collision in y
                    if self.vel_y < 0: #si esta saltando
                        dy = lista_plataformas_movimiento[i].rect.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0: #si esta cayendo
                        dy = lista_plataformas_movimiento[i].rect.top +1 - self.rect.bottom #el +1 para que no buggue animaciones
                        self.vel_y = 0
                        self.in_air = False
            for i in range(len(lista_de_trampas)): #verificar colision con trampas
                if lista_de_trampas[i].rect.colliderect(self.rect):
                    if flag_sonidos_colision == True:
                        self.sound_enemies_collision.play()
                    self.health_remaining -= 1
                    self.vel_y = -12
            enemigos_a_eliminar = [] #eliminar enemigos
            for i in range(len(lista_de_enemigos)): #verificar colision con enemigos
                if lista_de_enemigos[i].rect.colliderect(self.rect):
                    if self.esta_pegando == True:
                        enemigos_a_eliminar.append(i)
                        if flag_sonidos_colision == True:
                            self.sound_enemies_destroy.play()
                    else:
                        if flag_sonidos_colision == True:
                            self.sound_enemies_collision.play()
                        self.health_remaining -= 1
                        self.vel_y = -15
            for enemigo in enemigos_a_eliminar: #elimino
                del lista_de_enemigos[enemigo]
            enemigos_a_eliminar_flotantes = []#eliminar enemigos flotantes
            for i in range(len(lista_enemigos_flotantes)): #verificar colision con enemigos flotantes
                if lista_enemigos_flotantes[i].rect.colliderect(self.rect):
                    if self.esta_pegando == True:
                        enemigos_a_eliminar_flotantes.append(i)
                        if flag_sonidos_colision == True:
                            self.sound_enemies_destroy.play()
                    else:
                        if flag_sonidos_colision == True:
                            self.sound_enemies_collision.play()
                        self.health_remaining -= 1
                        self.vel_y = -15
            for enemigo in enemigos_a_eliminar_flotantes: #elimino
                del lista_enemigos_flotantes[enemigo]
            monedas_a_eliminar = [] #eliminar monedas
            for i in range(len(lista_de_monedas)): #verifico colision con monedas
                if lista_de_monedas[i].rect.colliderect(self.rect):
                    if flag_sonidos_colision == True:
                        self.sound_coins_collision.play()
                    self.score += 100
                    monedas_a_eliminar.append(i)
            for moneda in monedas_a_eliminar: #elimino
                del lista_de_monedas[moneda]
            vidas_a_eliminar = [] #eliminar vidas
            for i in range(len(lista_vidas)): #verifico colision con vidas
                if lista_vidas[i].rect.colliderect(self.rect):
                    if self.health_remaining < 20:
                        self.health_remaining += 1
                        vidas_a_eliminar.append(i)
            for vida in vidas_a_eliminar: #elimino
                del lista_vidas[vida]
            #movimiento de los rectangulos del personaje
            self.rect.x += dx
            self.rect.y += dy
    def animar(self, pantalla, lista):
        largo = len(lista)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        self.image = lista[self.contador_pasos]
        pantalla.blit(lista[self.contador_pasos], self.rect)
        self.contador_pasos += 1
    def reset(self, x, y, vida): #sirve para el constructor y para llamarlo cuando se muere
        self.image = pygame.image.load('salta\\0.png')
        self.image = pygame.transform.scale(self.image, (55,65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        self.sound_enemies_collision = pygame.mixer.Sound('musica\\colision_enemigos.mp3')
        self.sound_coins_collision = pygame.mixer.Sound('musica\\moneda_colision.mp3')
        sound_enemies_destroy = pygame.mixer.Sound('musica\\destroy_enemies.mp3')
        sound_enemies_destroy.set_volume(0.1)
        self.sound_enemies_destroy = sound_enemies_destroy
        self.game_over = 0
        self.score = 0
        self.health_start = vida
        self.health_remaining = vida
        self.time_shot = 0
        self.flag_derecha = True
        self.tiempo = 80
        self.contador_pasos = 0
        self.esta_pegando = False
        self.personaje_derecha_quieto = reescalar_imagenes(personaje_quieto_derecha, 55 , 65)
        self.personaje_derecha_camina = reescalar_imagenes(personaje_camina_derecha, 55, 65)
        self.personaje_derecha_salta = reescalar_imagenes(personaje_salta_derecha, 55, 65)
        self.personaje_derecha_dispara = reescalar_imagenes(personaje_dispara_derecha, 55, 65)
        self.personaje_derecha_mele = reescalar_imagenes(personaje_mele_derecha, 55, 65)
        self.personaje_izquierda_quieto = reescalar_imagenes(personaje_quieto_izquierda, 55, 65)
        self.personaje_izquierda_camina = reescalar_imagenes(personaje_camina_izquierda, 55, 65)
        self.personaje_izquierda_salta = reescalar_imagenes(personaje_salta_izquierda, 55, 65)
        self.personaje_izquierda_dispara = reescalar_imagenes(personaje_dispara_izquierda, 55, 65)
        self.personaje_izquierda_mele = reescalar_imagenes(personaje_mele_izquierda, 55, 65)