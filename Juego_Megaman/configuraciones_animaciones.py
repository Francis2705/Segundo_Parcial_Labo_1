import pygame

def girar_imagenes(lista_original_animaciones, flip_x, flip_y):
    lista_girada = []
    for imangen in lista_original_animaciones:
        lista_girada.append(pygame.transform.flip(imangen, flip_x, flip_y))
    return lista_girada
def reescalar_imagenes(lista_animaciones, ancho, alto):
    for i in range(len(lista_animaciones)):
        lista_animaciones[i] = pygame.transform.scale(lista_animaciones[i], (ancho, alto))
    return lista_animaciones

#Personaje
personaje_quieto_derecha = [
    pygame.image.load('quieto\\0.png'),
    pygame.image.load('quieto\\0.png'),
    pygame.image.load('quieto\\1.png'),
    pygame.image.load('quieto\\1.png'),
    pygame.image.load('quieto\\2.png'),
    pygame.image.load('quieto\\2.png')
]
personaje_camina_derecha = [
    pygame.image.load('camina\\0.png'),
    pygame.image.load('camina\\1.png'),
    pygame.image.load('camina\\2.png'),
    pygame.image.load('camina\\3.png'),
    pygame.image.load('camina\\4.png'),
    pygame.image.load('camina\\5.png'),
    pygame.image.load('camina\\6.png'),
    pygame.image.load('camina\\7.png'),
    pygame.image.load('camina\\8.png'),
    pygame.image.load('camina\\9.png'),
    pygame.image.load('camina\\10.png'),
    pygame.image.load('camina\\11.png')
]
personaje_salta_derecha = [
    pygame.image.load('salta\\2.png')
]
personaje_dispara_derecha = [
    pygame.image.load('dispara\\0.png'),
    pygame.image.load('dispara\\0.png'),
    pygame.image.load('dispara\\1.png'),
    pygame.image.load('dispara\\1.png'),
    pygame.image.load('dispara\\2.png'),
    pygame.image.load('dispara\\2.png')
]
personaje_mele_derecha = [
    pygame.image.load('ataque_mele\\0.png'),
    pygame.image.load('ataque_mele\\0.png'),
    pygame.image.load('ataque_mele\\1.png'),
    pygame.image.load('ataque_mele\\1.png'),
    pygame.image.load('ataque_mele\\2.png'),
    pygame.image.load('ataque_mele\\2.png')
]
try:
    personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)
    personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)
    personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)
    personaje_dispara_izquierda = girar_imagenes(personaje_dispara_derecha, True, False)
    personaje_mele_izquierda = girar_imagenes(personaje_mele_derecha, True, False)
except NameError as e:
    with open('errores.txt','a') as error:
        error.write(f'Error -> "{e}"\n')

#Trampas
trampa_sierra = [
    pygame.image.load('objetos\\trampa1.png'),
    pygame.image.load('objetos\\trampa1.png'),
    pygame.image.load('objetos\\trampa2.png'),
    pygame.image.load('objetos\\trampa2.png')
]
#Enemigos tierra
enemigo_derecha = [
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\0.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\1.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\2.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png'),
    pygame.image.load('enemigo\\3.png')
]
enemigo_izquierda = girar_imagenes(enemigo_derecha, True, False)
#Enemigos flotantes
enemigo_derecha_flota = [
    pygame.image.load('enemigo_flota\\0.png'),
    pygame.image.load('enemigo_flota\\0.png'),
    pygame.image.load('enemigo_flota\\1.png'),
    pygame.image.load('enemigo_flota\\1.png'),
    pygame.image.load('enemigo_flota\\2.png'),
    pygame.image.load('enemigo_flota\\2.png'),
    pygame.image.load('enemigo_flota\\3.png'),
    pygame.image.load('enemigo_flota\\3.png')
]
enemigo_izquierda_flota = girar_imagenes(enemigo_derecha_flota, True, False)
#Boss final
boss_final = [
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\0.png'),
    pygame.image.load('chatgpt\\1.png'),
    pygame.image.load('chatgpt\\1.png'),
    pygame.image.load('chatgpt\\1.png'),
    pygame.image.load('chatgpt\\1.png'),
    pygame.image.load('chatgpt\\1.png')
]