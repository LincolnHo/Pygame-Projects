from os import listdir
import sys, pygame

def load_image(name):
    image = pygame.image.load(name)
    return image

class LowerBodySprite(pygame.sprite.Sprite):
    __frameIndex = 0
    __frames = []
    __mode = 0
    def __init__(self):
        super(LowerBodySprite, self).__init__()
        self.loadFrames()

        self.image = self.__frames[self.__mode][self.__frameIndex]
        self.rect = pygame.Rect(30,60,358,353)

    def loadFrames(self):
        animList = ['idle','walk','run','strafe_left','strafe_right']

        for x in animList:
            curF = []
            for i in range(0,len(listdir('Top_Down_Survivor/feet/%s' % x))):
                curF.append(load_image('Top_Down_Survivor/feet/%s/survivor-%s_%d.png' % (x,x,i) ))
            self.__frames.append(curF)

    def setMode(self, m):
        self.__mode = m

    def update(self):
        if self.__frameIndex >= len(self.__frames[self.__mode]) : self.__frameIndex = 0
        self.image = self.__frames[self.__mode][self.__frameIndex]
        self.__frameIndex += 1

class UpperBodySprite(pygame.sprite.Sprite):
    __frameIndex = 0
    __frames = []
    __mode = 0
    __moving = False
    __ready = True
    def __init__(self):
        super(UpperBodySprite, self).__init__()
        self.rect = pygame.Rect(5,5,358,353)
    def setFrames(self, newframe):
        if self.__frames != newframe:
            self.__frameIndex = 0
            self.__frames = newframe
            self.image = self.__frames[self.__mode][self.__frameIndex]

    def setMode(self,m):
        self.__mode = m
        self.__frameIndex = 0
        if self.__mode != 0 and self.__mode != 1: self.__ready = False

    def setMove(self,m):
        if m:
            self.__moving = True
        else:
            self.__moving = False
    def getReady(self):
        return self.__ready
    def update(self):
        if self.__frameIndex >= len(self.__frames[self.__mode]) :

            if self.__moving:
                self.setMode(1)
            else:
                self.setMode(0)
            self.__ready = True
        self.image = self.__frames[self.__mode][self.__frameIndex]

        self.__frameIndex += 1

class PlayerSprite(pygame.sprite.Group):
    """Group UpperBodySprite and LowerBodySprite together"""

    __animCount = 0
    __timer  = 2

    def __init__(self):
        super(PlayerSprite, self).__init__()
        self.__ubSprite = UpperBodySprite()
        self.__lbSprite = LowerBodySprite()

        self.add(self.__lbSprite)
        self.add(self.__ubSprite)
    def update(self):
        self.__animCount -= 1
        if self.__animCount < 0:
            self.__ubSprite.update()
            self.__lbSprite.update()
            self.__animCount = self.__timer
    def getReadyForInput(self):
        return self.__ubSprite.getReady()

    def movePlayer(self,x,y):
        if x == 0 and y == 0:
            self.__ubSprite.setMove(False)
            return
        else:
            self.__ubSprite.rect.x += x
            self.__ubSprite.rect.y += y
            self.__lbSprite.rect.x += x
            self.__lbSprite.rect.y += y
            self.__ubSprite.setMove(True)
    def actionAnim(self, mode):
        self.__ubSprite.setMode(mode)
    def changeWeapon(self, frames):
        self.__ubSprite.setMode(0)
        self.__ubSprite.setFrames(frames)
