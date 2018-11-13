import pygame
from settings import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, x,y,w,h,game):
        super(Platform, self).__init__()
        self.image = pygame.Surface((w,h))
        self.game = game
        self.loadSprite()
        self.image = self.grassTiles
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.top = y

    def loadSprite(self):
        self.grassTiles = self.game.u.blitImage(self.game.tileSheet,117,0,35,14)
