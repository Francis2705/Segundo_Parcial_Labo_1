import pygame

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        pygame.sprite.Sprite.__init__(self) #inicializo la clase base de sprites y esto me permite tener las demas funcionalidades
        self.image = pygame.image.load('objetos\\disparo.png')
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direccion = direccion
    def update(self, pantalla, lista_de_enemigos, player, lista_enemigos_flotantes, lista_boss_final, flag_sonidos_colision):
        pantalla.blit(self.image, self.rect)
        if self.direccion == 1:
            self.rect.x += 20
        else:
            self.rect.x -= 20

        for i in range(len(lista_boss_final)):
            if self.rect.colliderect(lista_boss_final[i]):
                lista_boss_final[i].health_remaining -= 1
                player.score += 5
                self.kill()

        if self.rect.colliderect(player.rect):
            player.health_remaining -= 1
            player.vel_y = -15
            self.kill()

        if self.rect.left < -5 or self.rect.right > 1220:
            self.kill()

        enemigos_a_eliminar = []
        for i in range(len(lista_de_enemigos)):
            if self.rect.colliderect(lista_de_enemigos[i]):
                if player.tiempo > 60:
                    player.score += 50
                else:
                    player.score += 25
                enemigos_a_eliminar.append(i)
                if flag_sonidos_colision == True:
                    player.sound_enemies_destroy.play()
                self.kill()
        for enemigo in enemigos_a_eliminar:
            del lista_de_enemigos[enemigo]

        enemigos_a_eliminar_flotantes = []
        for i in range(len(lista_enemigos_flotantes)):
            if self.rect.colliderect(lista_enemigos_flotantes[i]):
                if player.tiempo > 60:
                    player.score += 50
                else:
                    player.score += 25
                enemigos_a_eliminar_flotantes.append(i)
                if flag_sonidos_colision == True:
                    player.sound_enemies_destroy.play()
                self.kill()
        for enemigo in enemigos_a_eliminar_flotantes:
            del lista_enemigos_flotantes[enemigo]