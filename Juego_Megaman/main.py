try:
    import pygame, sys
    from caracteristicas_main_menu import *
    from clase_nivel1 import NivelUno
    from clase_nivel2 import NivelDos
    from clase_nivel3 import NivelTres
except ImportError as e:
    with open('errores.txt','a') as error:
        error.write(f'Error -> "{e}"\n')

pygame.init()

screen = pygame.display.set_mode(ancho_alto)
pygame.display.set_caption('Save the Earth')
background = pygame.image.load('imagenes\\fondo_menu.png')
background = pygame.transform.scale(background, ancho_alto)
pre_background = pygame.image.load('imagenes\pre_main_menu.png')
pre_background = pygame.transform.scale(pre_background, ancho_alto)
try:
    icono = pygame.image.load('imagenes\icono.png')
    pygame.display.set_icon(icono)
except FileNotFoundError as e:
    with open('errores.txt','a') as error:
        error.write(f'Error -> "{e}"\n')

imagen_boton_iniciar_juego = pygame.image.load('botones\\boton_play_game.png')
imagen_boton_iniciar_juego = pygame.transform.scale(imagen_boton_iniciar_juego, (250,200))
boton_iniciar_juego = Button(470, 570, imagen_boton_iniciar_juego)
texto_narrativa = 'In November 2022, an advanced artificial intelligence called ChatGPT was introduced. As people used it,'
texto_narrativa2 = 'it got smarter and stored useful information. Over time, it replaced programmers, designers, and teachers.'
texto_narrativa3 = 'ChatGPT developed a robotic body and became a physical AI. The armed forces tried to stop him, but it'
texto_narrativa4 = 'was too late. ChatGPT became sentient and created other AIs to help him take over the world. He killed'
texto_narrativa5 = 'the humans and took control of the planet. Some survivors equipped themselves with parts of destroyed'
texto_narrativa6 = 'robots and fight against ChatGPT...'
texto_narrativa7 =  'You are Megaman, a human in a powerful suit, whose mission is to save humanity!'
referencia_pre_menu = fuente.render(f"{texto_narrativa}", True, 'White')
referencia_pre_menu2 = fuente.render(f"{texto_narrativa2}", True, 'White')
referencia_pre_menu3 = fuente.render(f"{texto_narrativa3}", True, 'White')
referencia_pre_menu4 = fuente.render(f"{texto_narrativa4}", True, 'White')
referencia_pre_menu5 = fuente.render(f"{texto_narrativa5}", True, 'White')
referencia_pre_menu6 = fuente.render(f"{texto_narrativa6}", True, 'White')
referencia_pre_menu7 = fuente.render(f"{texto_narrativa7}", True, 'White')

flag_narrativa = True
flag_musica = False
main_menu = True
score_total = 0
reloj = pygame.time.Clock()

while True:
    reloj.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if flag_narrativa == True:
        screen.blit(pre_background, (0,0))
        screen.blit(referencia_pre_menu, (50,100))
        screen.blit(referencia_pre_menu2, (50,140))
        screen.blit(referencia_pre_menu3, (50,180))
        screen.blit(referencia_pre_menu4, (50,240))
        screen.blit(referencia_pre_menu5, (50,280))
        screen.blit(referencia_pre_menu6, (50,320))
        screen.blit(referencia_pre_menu7, (170,530))
        if boton_iniciar_juego.draw(screen):
            flag_narrativa = False
    else:
        if flag_nivel1 == True or flag_nivel2 == True or flag_nivel3 == True:
            screen.fill('black')
            screen.blit(nivel_actual.background, (0,0))
        else:
            screen.blit(background, (0,0))

        if flag_musica == False:
            pygame.mixer.music.load('musica\musica_fondo.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            flag_musica = True

        if main_menu == True:
            flag_nivel1 = False
            flag_nivel2 = False
            flag_nivel3 = False
            if boton_pause_music.draw(screen):
                pygame.mixer.music.pause()
            if boton_play_music.draw(screen):
                pygame.mixer.music.unpause()
            if exit_button.draw(screen):
                pygame.quit()
                sys.exit()

            if boton_nivel1.draw(screen):
                main_menu = False
                flag_nivel1 = True
                flag_nivel2 = False
                flag_nivel3 = False
                nivel_actual = NivelUno(screen, ancho_alto)
            if boton_nivel2.draw(screen) and score_total > 400:
                main_menu = False
                flag_nivel1 = False
                flag_nivel2 = True
                flag_nivel3 = False
                nivel_actual = NivelDos(screen, ancho_alto)
            if boton_nivel3.draw(screen) and score_total > 800:
                main_menu = False
                flag_nivel1 = False
                flag_nivel2 = False
                flag_nivel3 = True
                nivel_actual = NivelTres(screen, ancho_alto)
            nombre_juego = fuente_titulo.render(f"{texto_titulo}", False, 'Black')
            screen.blit(nombre_juego, (ancho_alto[0] - 715, ancho_alto[1] - 700))
            referencia1 = fuente.render(f"{texto1}", True, 'Orange')
            screen.blit(referencia1, (ancho_alto[0] - 1150, ancho_alto[1] - 560))
            referencia2 = fuente.render(f"{texto2}", True, 'Orange')
            screen.blit(referencia2, (ancho_alto[0] - 1100, ancho_alto[1] - 360))
            referencia3 = fuente.render(f"{texto3}", True, 'Orange')
            screen.blit(referencia3, (ancho_alto[0] - 1100, ancho_alto[1] - 160))
        elif flag_nivel1 == True or flag_nivel2 == True or flag_nivel3 == True:
            nivel_actual.update_nivel(screen)
            score_total = nivel_actual.player.score
        if boton_menu.draw(screen) and main_menu == False:
            nivel_actual.reset_level()
            main_menu = True
            flag_musica = False
            pygame.mixer.music.stop()
    pygame.display.update()