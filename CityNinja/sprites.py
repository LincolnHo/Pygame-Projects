# Sprite classe
from settings import *
import pygame,sys

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super(Player, self).__init__()
        self.game = game
        self.image = pygame.Surface((30,30))
        image = pygame.image.load(PLAYER_IMAGE)
        image = pygame.transform.smoothscale(image, (120,120))
        self.image.blit(image,(-42,-45))

        self.rImage = self.image
        self.lImage = pygame.transform.flip(self.image, True, False)
        #self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(WIDTH/2,HEIGHT/2)
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
        self.facingRight = True
        self.headBand = self.addHeadBand()

    def addHeadBand(self):
        headBand = pygame.sprite.Sprite()
        headBand.image = pygame.Surface((40,40))
        headBand.image.set_colorkey(BLACK)
        image = pygame.image.load(PLAYER_BAND)
        image = pygame.transform.smoothscale(image,(40,40))
        self.rhI = image
        self.lhI = pygame.transform.flip(self.rhI, True, False)
        headBand.image.blit(image,(0,0))
        headBand.rect = headBand.image.get_rect()
        return headBand
    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self,self.game.platform_sprites,False)
        if hits:
            self.vel.y = -PLAYER_JUMP

        self.rect.y -= 1
        if (self.pos.x <= self.image.get_width() or self.pos.x >= (WIDTH - self.image.get_width())):
            self.vel.y = -PLAYER_JUMP * 0.7
            if self.rect.left <= self.image.get_width()/2:
                self.rect.x = self.image.get_width()
                self.vel.x += PLAYER_JUMP * 0.5
            if self.rect.right >= (WIDTH - self.image.get_width()/2):
                self.rect.x = WIDTH - (self.image.get_width() * 1.5)
                self.vel.x -= PLAYER_JUMP * 0.5


    def update(self):
        self.acc = pygame.math.Vector2(0,PLAYER_GRAV)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -PLAYER_ACC
        elif keys[pygame.K_d]:
            self.acc.x = PLAYER_ACC

        #slow down player falling if they are touching either wall
        if self.pos.x == self.image.get_width()/2 or self.pos.x == (WIDTH - self.image.get_width()/2):
            if self.vel.y > 0 : self.acc.y *= 0.3

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc


        #adjusting sprite transformation when it's touching walls
        if self.rect.right > WIDTH :
            self.pos.x = WIDTH - self.image.get_width()/2
            self.facingRight = False
            self.vel.x = 0
            self.acc.x = 0
        if self.rect.left < 0:
            self.pos.x = self.image.get_width()/2
            self.facingRight = True
            self.vel.x = 0
            self.acc.x = 0




        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        if self.vel.x > 0 :
            self.facingRight = True
        elif self.vel.x < 0:
            self.facingRight = False


        if self.facingRight:
            self.image = self.rImage
            self.headBand.image = self.rhI
        else:
            self.image = self.lImage
            self.headBand.image = self.lhI

        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):

    def __init__(self, x,y,w,h,img):
        super(Platform, self).__init__()
        self.image = pygame.Surface((w,h))
        self.image.blit(img,(0,0),(1200,400,w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
