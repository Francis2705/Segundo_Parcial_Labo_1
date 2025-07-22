import pygame
from clase_boton import Button

pygame.font.init()
ancho_alto = (1200, 800)
#buttons
exit_image = pygame.image.load('botones/exit.png')
exit_image = pygame.transform.scale(exit_image, (200, 100))
try:
    exit_button = Button(ancho_alto[0] - 210, ancho_alto[1] - 110, exit_image)
except TypeError as e:
    with open('errores.txt','a') as error:
        error.write(f'Error -> "{e}"\n')
#botones niveles
fuente_titulo = pygame.font.SysFont('8bitoperator', 40)
texto_titulo = 'SAVE THE EARTH'
imagen_nivel1 = pygame.image.load('botones\\nivel1.png')
imagen_nivel1 = pygame.transform.scale(imagen_nivel1, (100,100))
boton_nivel1 = Button(ancho_alto[0] - 650, ancho_alto[1] - 600, imagen_nivel1)
flag_nivel1 = False
texto1 = """The adventures begins, destroy the robots!"""
imagen_nivel2 = pygame.image.load('botones\\nivel2.png')
imagen_nivel2 = pygame.transform.scale(imagen_nivel2, (100,100))
boton_nivel2 = Button(ancho_alto[0] - 650, ancho_alto[1] - 400, imagen_nivel2)
flag_nivel2 = False
texto2 = 'Clear the way! (You need 400 points)'
imagen_nivel3 = pygame.image.load('botones\\nivel3.png')
imagen_nivel3 = pygame.transform.scale(imagen_nivel3, (100,100))
boton_nivel3 = Button(ancho_alto[0] - 650, ancho_alto[1] - 200, imagen_nivel3)
flag_nivel3 = False
texto3 = 'Kill ChatGPT! (You need 800 points)'
fuente = pygame.font.SysFont('8bitoperator', 32)
#boton menu principal
imagen_boton_menu = pygame.image.load('botones\home.png')
imagen_boton_menu = pygame.transform.scale(imagen_boton_menu, (75,75))
boton_menu = Button(ancho_alto[0] - 80, ancho_alto[1] - 780, imagen_boton_menu)
#botones sonido
imagen_boton_sonido_play = pygame.image.load('botones\sonido_play.png')
imagen_boton_sonido_play = pygame.transform.scale(imagen_boton_sonido_play, (50,50))
boton_play_music = Button(ancho_alto[0] - 65, ancho_alto[1] - 610, imagen_boton_sonido_play)
imagen_boton_sonido_pause = pygame.image.load('botones\sonido_pause.png')
imagen_boton_sonido_pause = pygame.transform.scale(imagen_boton_sonido_pause, (50,50))
boton_pause_music = Button(ancho_alto[0] - 65, ancho_alto[1] - 680, imagen_boton_sonido_pause)