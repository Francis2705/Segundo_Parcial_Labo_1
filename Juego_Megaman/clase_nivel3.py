import pygame
from clase_personaje import Player
from clase_plataforma import Platform
from clase_estrella import Coin
from clase_vida_extra import Health
from clase_boton import Button
from clase_boss_final import BossFinal

class NivelTres():
    def __init__(self, screen, ancho_alto):
        self.screen = screen
        self.ancho_alto = ancho_alto
        self.background = pygame.image.load('imagenes\\fondo3.png')
        self.background = pygame.transform.scale(self.background, self.ancho_alto)
        self.win_background = pygame.image.load('imagenes\pantalla_win.png')
        self.win_background = pygame.transform.scale(self.win_background, self.ancho_alto)
        self.lose_background = pygame.image.load('imagenes\pantalla_lose.png')
        self.lose_background = pygame.transform.scale(self.lose_background, self.ancho_alto)

        #sonido fondo
        pygame.mixer.music.load('musica\\nivel_3.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        imagen_boton_sonido_play = pygame.image.load('botones\sonido_play.png')
        imagen_boton_sonido_play = pygame.transform.scale(imagen_boton_sonido_play, (50,50))
        self.boton_play_music = Button(610, 280, imagen_boton_sonido_play)
        imagen_boton_sonido_pause = pygame.image.load('botones\sonido_pause.png')
        imagen_boton_sonido_pause = pygame.transform.scale(imagen_boton_sonido_pause, (50,50))
        self.boton_pause_music = Button(530, 280, imagen_boton_sonido_pause)
        #desactivar sonidos colision
        imagen_boton_pausa = pygame.image.load('botones\\activar_sonido_colision.png')
        imagen_boton_pausa = pygame.transform.scale(imagen_boton_pausa, (50,50))
        self.boton_pausa_sonidos = Button(570, 340,imagen_boton_pausa)
        self.flag_sonidos_colision = True

        self.fuente = pygame.font.SysFont('helvetica', 50)
        self.moneda_imagen = pygame.image.load('objetos\coin.png')
        self.moneda_imagen = pygame.transform.scale(self.moneda_imagen, (40, 40))

        self.reset_level()

        #buttons
        restart_image = pygame.image.load('botones\\restart1.png')
        restart_image = pygame.transform.scale(restart_image, (300, 100))
        restart_button = Button(200, 400, restart_image)
        self.restart_button = restart_button
        #botones de pausa y play
        imagen_boton_play = pygame.image.load('botones\\boton_play.png')
        imagen_boton_play = pygame.transform.scale(imagen_boton_play, (50,50))
        boton_play = Button(ancho_alto[0] - 310, ancho_alto[1] - 780, imagen_boton_play)
        self.boton_play = boton_play

        imagen_boton_pausa = pygame.image.load('botones\\boton_pausa.png')
        imagen_boton_pausa = pygame.transform.scale(imagen_boton_pausa, (50,50))
        boton_pausa = Button(ancho_alto[0] - 210, ancho_alto[1] - 780, imagen_boton_pausa)
        self.boton_pausa = boton_pausa
        self.flag_pausa = False

        #cronometro
        self.tiempo_transcurrido2 = 0
        self.score_total = 0

    def update_nivel(self, screen):
        if self.player.game_over == 0:
            if len(self.lista_boss_final) == 0: 
                self.player.game_over = 1
            else:
                if self.flag_pausa == True: #aca hago las settings
                    screen.fill('Gray')
                    settings = self.fuente.render(f"Settings", True, 'Black')
                    screen.blit(settings, (525,200))
                    if self.boton_pause_music.draw(screen):
                        pygame.mixer.music.pause()
                    if self.boton_play_music.draw(screen):
                        pygame.mixer.music.unpause()
                    if self.boton_pausa_sonidos.draw(screen):
                        self.flag_sonidos_colision = not self.flag_sonidos_colision
                    if self.boton_play.draw(screen):
                        self.flag_pausa = False
                else: #este else es el del juego principal
                    if self.boton_pausa.draw(screen):
                        self.flag_pausa = True
                    self.player.update(screen, self.lista_plataformas, self.lista_trampas, self.lista_enemigos, self.lista_monedas, 
                                    self.lista_plataformas_movimiento, self.bullet_group, self.lista_vidas, 
                                    self.lista_enemigos_flotantes, self.rectangulo_final, self.flag_sonidos_colision)
                    self.platform.update(screen, self.lista_plataformas)
                    self.coin1.update(screen, self.lista_monedas)
                    self.vida1.update(screen, self.lista_vidas)
                    self.bullet_group.update(screen, self.lista_enemigos, self.player, self.lista_enemigos_flotantes, 
                                            self.lista_boss_final, self.flag_sonidos_colision)
                    
                    self.bullet_group_boss.update(screen, self.player)
                    self.boss_final.update(screen, self.lista_boss_final, self.bullet_group, self.player, self.bullet_group_boss)
                    
                    puntaje = self.fuente.render(f": {self.player.score}", True, 'Red') #score
                    screen.blit(puntaje, (60,4))
                    screen.blit(self.moneda_imagen, (10,12))
                    minutes = self.player.tiempo // 60
                    seconds = self.player.tiempo % 60
                    time_string = "{:02d}:{:02d}".format(minutes, seconds) #cronometro
                    text = self.fuente.render(time_string, True, 'Red')
                    screen.blit(text, (30,80))
                    self.tiempo_transcurrido = pygame.time.get_ticks()
                    if self.tiempo_transcurrido - self.tiempo_transcurrido2 >= 1000:
                        self.tiempo_transcurrido2 = self.tiempo_transcurrido
                        self.player.tiempo -= 1
                    if self.player.tiempo == 0:
                        self.player.game_over = -1
        elif self.player.game_over == -1:
            self.player.health_remaining = 0
            self.player.score = 0
            perdio = self.fuente.render(f"You lost! Don't give up!", True, 'White')
            screen.blit(self.lose_background, (0,0))
            screen.blit(perdio, (175,300))
            if self.restart_button.draw(screen):
                self.reset_level()
        elif self.player.game_over == 1:
            self.score_total = self.player.score
            gano = self.fuente.render(f"Congratulations! You save the humanity", True, 'White')
            screen.blit(self.win_background, (0,0))
            screen.blit(gano, (450,650))

    def reset_level(self):
        self.player = Player(50, 520, 20)

        self.platform = Platform(-2,799,1202,2) #piso
        self.platform2 = Platform(75, 700, 120, 25)
        self.platform3 = Platform(265, 650, 100, 25)
        self.platform4 = Platform(120, 550, 100, 25)
        self.platform5 = Platform(265, 450, 100, 25)
        self.platform6 = Platform(120, 350, 100, 25)
        lista_plataformas = []
        lista_plataformas.append(self.platform)
        lista_plataformas.append(self.platform2)
        lista_plataformas.append(self.platform3)
        lista_plataformas.append(self.platform4)
        lista_plataformas.append(self.platform5)
        lista_plataformas.append(self.platform6)

        self.boss_final = BossFinal(800, 500, 1)
        lista_boss_final = []
        lista_boss_final.append(self.boss_final)

        self.coin1 = Coin(165, 285, 20, 20, 1)
        self.coin2 = Coin(165, 500, 20, 20, -1)
        self.coin3 = Coin(420, 245, 20, 20, 1)
        self.coin5 = Coin(420, 330, 20, 20, 1)
        self.coin6 = Coin(420, 415, 20, 20, 1)
        self.coin7 = Coin(420, 500, 20, 20, 1)
        self.coin8 = Coin(420, 585, 20, 20, 1)
        self.coin9 = Coin(150, 665, 20, 20, 1)
        self.coin10 = Coin(30, 210, 20, 20, 1)
        self.coin11 = Coin(430, 770, 20, 20, 1)
        lista_monedas = []
        lista_monedas.append(self.coin1)
        lista_monedas.append(self.coin2)
        lista_monedas.append(self.coin3)
        lista_monedas.append(self.coin5)
        lista_monedas.append(self.coin6)
        lista_monedas.append(self.coin7)
        lista_monedas.append(self.coin8)
        lista_monedas.append(self.coin9)
        lista_monedas.append(self.coin10)
        lista_monedas.append(self.coin11)

        self.vida1 = Health(30, 300, 20, 20, 1)
        self.vida2 = Health(30, 400, 20, 20, 1)
        self.vida3 = Health(30, 500, 20, 20, 1)
        self.vida4 = Health(30, 600, 20, 20, 1)
        self.vida5 = Health(30, 700, 20, 20, 1)
        self.vida6 = Health(310, 410, 20, 20, -1)
        self.vida7 = Health(310, 620, 20, 20, -1)
        lista_vidas = []
        lista_vidas.append(self.vida1)
        lista_vidas.append(self.vida2)
        lista_vidas.append(self.vida3)
        lista_vidas.append(self.vida4)
        lista_vidas.append(self.vida5)
        lista_vidas.append(self.vida6)
        lista_vidas.append(self.vida7)

        self.lista_plataformas = lista_plataformas
        self.lista_enemigos = []
        self.lista_monedas = lista_monedas
        self.lista_vidas = lista_vidas
        self.lista_boss_final = lista_boss_final
        self.lista_trampas = []
        self.lista_plataformas_movimiento = []
        self.lista_enemigos_flotantes = []
        self.bullet_group = pygame.sprite.Group()
        self.bullet_group_boss = pygame.sprite.Group()
        self.rectangulo_final = pygame.Rect(610, 1, 580, 800)