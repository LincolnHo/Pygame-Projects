import pygame
import random

WHITE = (255,255,255)

class Mob(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super(Mob, self).__init__()
        self.image = pygame.Surface((32,32))
        self.image = pygame.image.load('bat.png')
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        side = random.randint(0,2)
        if side == 0: self.rect.x = 0
        if side == 1: self.rect.x = x -50
        self.rect.y = y
        self.speedX = random.randint(-6,-3)
        self.speedY = random.randint(-4,3)
        if self.speedY == 0: self.speedY += 1

    def changeSpeed(self,modX,modY):
        self.speedX *= modX
        self.speedY *= modY
    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.left <0 or self.rect.left > 750 : self.changeSpeed(-1,1)
        if self.rect.top < 0 or self.rect.bottom > 500 : self.changeSpeed (1,-1)
