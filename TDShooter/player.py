import sys,pygame

from weapon import Weapon
from sprite import PlayerSprite

class Player():
    """Holds weapons, sprites and various stats"""

    __playerName = ""
    __hitpoint = 0


    __moving = False
    __sprint = False
    __strafing = (False,False)

    __walkSpeed = 5
    __sprintMod = 2
    __strafeMod = 0.6

    __fire = False
    __reload = False
    __melee = False

    __weapon = 0
    __bulletInClip = [0,0,0,0,0]

    __ammo = [0,0,80,200,40]


    def __init__(self, name):
        self.__playerName = name
        self.__weapon = Weapon()
        self.sprite = PlayerSprite()
        self.changeWeapon(0)

    def fire(self):
        if self.__bulletInClip[self.__weapon.getWeaponCode()] > 0 and self.sprite.getReadyForInput():
            self.__fire = True
            self.__bulletInClip[self.__weapon.getWeaponCode()] -= 1
            self.sprite.actionAnim(3)

    def reload(self):

        if self.__bulletInClip[self.__weapon.getWeaponCode()] == self.__weapon.getClipSize() or self.__ammo[self.__weapon.getWeaponCode()]  == 0:
            return

        self.__reload = True
        if self.__ammo[self.__weapon.getWeaponCode()] < self.__weapon.getClipSize() and self.sprite.getReadyForInput():
            self.__bulletInClip[self.__weapon.getWeaponCode()]  = self.__ammo[self.__weapon.getWeaponCode()]
            self.modAmmo(-self.__bulletInClip[self.__weapon.getWeaponCode()] )
        else:
            self.__bulletInClip[self.__weapon.getWeaponCode()]  = self.__weapon.getClipSize()
            self.modAmmo(-self.__weapon.getClipSize())
        self.sprite.actionAnim(4)
    def melee(self):
        if self.sprite.getReadyForInput(): self.sprite.actionAnim(2)
    def changeWeapon(self, code):
        self.__weapon.changeWeapon(code)
        self.sprite.changeWeapon(self.__weapon.getFrames())

    def movePlayer(self, horizontal, vertical):
        self.setMoving(True)
        self.__strafing = (False, False)
        if vertical == 1 : self.__strafing = (False, True)
        if vertical == -1 : self.__strafing = (True, False)
        self.sprite.movePlayer(horizontal * (self.__walkSpeed + int(self.__sprint) * self.__sprintMod) , vertical * self.__walkSpeed)
    def getMoving(self):
        return self.__moving
    def getSprinting(self):
        return self.__sprint

    def setMoving(self, b):
        self.__moving = b
    def setSprinting(self,b):
        self.__sprint = b

    def getHP(self):
        return self.__hitpoint
    def modHP(self,mod):
        self.__hitpoint += mod

    def getBulletInClip(self):
        return self.__bulletInClip[self.__weapon.getWeaponCode()]
    def getAmmo(self):
        return self.__ammo[self.__weapon.getWeaponCode()]
    def modAmmo(self, s):
        self.__ammo[self.__weapon.getWeaponCode()] += s
