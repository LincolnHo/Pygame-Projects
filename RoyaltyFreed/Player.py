import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Player, self).__init__()
        self.game = game
        self.loadFrames()
        #initial image
        self.image = self.walkFrameR[0]
        self.rect = self.image.get_rect()


        #movement variables
        self.pos = pygame.math.Vector2(WIDTH/2,HEIGHT/2)
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)

        self.jumpPower = 0

        self.walking = False
        self.sprinting = False
        self.jumping = False
        #animation variables
        self.currentFrame = 0
        self.lastUpdate = 0


    def loadFrames(self):
        self.walkFrameR = []
        self.walkFrameR.append(self.game.u.blitImage(self.game.spriteSheet,9,42,15,22))
        self.walkFrameR.append(self.game.u.blitImage(self.game.spriteSheet,41,41,15,22))
        self.walkFrameR.append(self.game.u.blitImage(self.game.spriteSheet,72,42,15,22))
        self.walkFrameR.append(self.game.u.blitImage(self.game.spriteSheet,104,41,15,22))
        self.walkFrameL = []
        for i in self.walkFrameR:
            self.walkFrameL.append(pygame.transform.flip(i,True,False))

        self.jumpFrameR = []
        self.jumpFrameR.append(self.game.u.blitImage(self.game.spriteSheet,135,43,17,21))
        self.jumpFrameR.append(self.game.u.blitImage(self.game.spriteSheet,168,41,16,22))
        self.jumpFrameR.append(self.game.u.blitImage(self.game.spriteSheet,201,41,15,22))
        self.jumpFrameR.append(self.game.u.blitImage(self.game.spriteSheet,233,43,16,21))

        self.jumpFrameL = []
        for i in self.jumpFrameR:
            self.jumpFrameL.append(pygame.transform.flip(i,True,False))

    def jump(self):
        self.rect.y +=1
        hits =  pygame.sprite.spritecollide(self,self.game.platform_sprites,False)
        if hits:
            self.vel.y = -(PLAYER_JUMP+self.jumpPower)
            self.jumpPower = 0
            self.jumping = True
        self.rect.y -= 1

    def jumpCut(self):
        if self.vel.y < -6 :self.vel.y = -6
    def update(self):
        self.acc = pygame.math.Vector2(0,PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_d]:
            self.acc.x = PLAYER_ACC




        self.acc.x += self.vel.x * -PLAYER_FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.1: self.vel.x = 0

        if not self.sprinting and self.vel.x != 0:
            self.vel.x = (self.vel.x / abs(self.vel.x)) * min(PLAYER_WALK_MAX, abs(self.vel.x))



        self.pos += self.vel + 0.5 * self.acc


        self.rect.midbottom = self.pos


        self.anim()
    def anim(self):
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        '''if not self.walking and not self.jumping:
            if now - self.lastUpdate > 200:
                self.lastUpdate = now
                bottom = self.rect.bottom
                left = self.rect.left
                if self.jumpPower != 0:
                    if self.image in self.walkFrameR: self.image = self.jumpFrameR[0]
                    if self.image in self.walkFrameL: self.image = self.jumpFrameL[0]
                else:
                    if self.image == self.jumpFrameR[0]: self.image = self.walkFrameR[0]
                    if self.image == self.jumpFrameL[0]: self.image = self.walkFrameL[0]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left'''

        if self.walking and not self.jumping:
            if now - self.lastUpdate > 200:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walkFrameR)
                bottom = self.rect.bottom
                left = self.rect.left
                if self.vel.x >= 0: self.image = self.walkFrameR[self.currentFrame]
                if self.vel.x < 0: self.image = self.walkFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left
        if self.walking and self.sprinting and not self.jumping:
            if now - self.lastUpdate > 200:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walkFrameR)
                bottom = self.rect.bottom
                left = self.rect.left
                if self.vel.x >= 0: self.image = self.walkFrameR[self.currentFrame]
                if self.vel.x < 0: self.image = self.walkFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left
        if self.vel.y !=0:
            if now - self.lastUpdate > 200:
                self.lastUpdate = now
                bottom = self.rect.bottom
                left = self.rect.left
                if self.vel.y <= 0: self.currentFrame = 1
                if self.vel.y > 0: self.currentFrame = 2
                if self.vel.x > 0: self.image = self.jumpFrameR[self.currentFrame]
                if self.vel.x < 0: self.image = self.jumpFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.left = left


        self.image.set_colorkey((0,0,0))
