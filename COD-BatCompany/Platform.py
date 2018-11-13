import pygame


GREEN = (0,255,0)
BLUE = (0,0,255)

class Ground(pygame.sprite.Sprite):
    def __init__(self,w,h):
        super(Ground, self).__init__()
        self.image = pygame.Surface((w,h/6))
        image = pygame.image.load('bridge.png')
        self.image.blit(image,(0,-400))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.top = h*5/6

    def update(self):
        pass

class Block(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super(Block, self).__init__()
        self.image = pygame.Surface((275,20))
        image = pygame.image.load('bridge.png')
        self.image.blit(image,(0,0),(600,400,600,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
