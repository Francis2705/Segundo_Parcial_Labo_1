import pygame

class BulletsBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        pygame.sprite.Sprite.__init__(self) #inicializo la clase base de sprites y esto me permite tener las demas funcionalidades
        self.image = pygame.image.load('objetos\\proyectil_boss.png')
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.direccion = direccion
    def update(self, pantalla, player):
        pantalla.blit(self.image, self.rect)
        self.rect.x -= 10
        if self.rect.colliderect(player.rect):
            player.health_remaining -= 5
            self.kill()
        if self.rect.left < -5 or self.rect.right > 1220:
            self.kill()