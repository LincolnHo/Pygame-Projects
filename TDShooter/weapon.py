from os import listdir

import sys,pygame,os

class Weapon():

    """The list images stores all the frames for the weapon
    0 - idle
    1 - walking
    2 - meleeattack
    3 - shoot
    4 - reload"""
    __weapon = 0

    __canFire = False
    __canMelee = False

    __firing = False
    __reloading = False
    __meleeing = False

    __images = []
    __values = []

    def __init__(self):
        self.loadFrames()
        self.loadValues()

    def load_image(self,name):
        image = pygame.image.load(name)
        return image

    def loadValues(self):
        f = open('stat.txt','r')
        for line in f:
            curline = []
            if (line.split(",")[0]) != "name":
                curline = line.split(",")

                self.__values.append(curline)



    def getWeaponName(self):
        return self.__values[0][0]
    def getFireDamage(self):
        return int(self.__values[self.__weapon][1])

    def getMeleeDamage(self):
        return int(self.__values[self.__weapon][2])

    def getClipSize(self):
        return int(self.__values[self.__weapon][3])

    def getFireCD(self):
        return int(self.__values[self.__weapon][4])

    def getReloadCD(self):
        return int(self.__values[self.__weapon][5])

    def getMeleeCD(self):
        return int(self.__values[self.__weapon][6])

    def getWeaponCode(self):
        return self.__weapon

    def changeWeapon(self,value):
        self.__weapon = value

    def getFrames(self):
        return self.__images[self.__weapon]

    def loadFrames(self):
        weaponList = ["flashlight","knife","handgun","rifle","shotgun"]
        mode = ["idle","move","meleeattack","shoot","reload"]

        for wp in weaponList:
            curWeapon = []
            for m in mode:
                curAnim = []
                if (os.path.isdir('Top_Down_Survivor/%s/%s' % (wp,m))):
                    for x in range (0,len(listdir('Top_Down_Survivor/%s/%s' % (wp,m)))):
                        curAnim.append(self.load_image('Top_Down_Survivor/%s/%s/survivor-%s_%s_%d.png' % (wp,m,m,wp, x)))
                curWeapon.append(curAnim)
            self.__images.append(curWeapon)

        '''for x in range (0,len(listdir('Top_Down_Survivor/%s/idle' % self.__name))):
            idle.append(self.load_image('Top_Down_Survivor/%s/idle/survivor-idle_%s_%d.png' % (self.__name, self.__name, x)))

        for x in range (0,len(listdir('Top_Down_Survivor/%s/move' % self.__name))):
            walking.append(self.load_image('Top_Down_Survivor/%s/move/survivor-move_%s_%d.png' % (self.__name, self.__name, x)))

        for x in range (0,len(listdir('Top_Down_Survivor/%s/meleeattack' % self.__name))):
            melee.append(self.load_image('Top_Down_Survivor/%s/meleeattack/survivor-meleeattack_%s_%d.png' % (self.__name, self.__name, x)))

        if (os.path.isdir('Top_Down_Survivor/%s/shoot' % self.__name)):
            for x in range (0,len(listdir('Top_Down_Survivor/%s/shoot' % self.__name))):
                firing.append(self.load_image('Top_Down_Survivor/%s/shoot/survivor-shoot_%s_%d.png' % (self.__name, self.__name, x)))

            for x in range (0,len(listdir('Top_Down_Survivor/%s/reload' % self.__name))):
                reloading.append(self.load_image('Top_Down_Survivor/%s/reload/survivor-reload_%s_%d.png' % (self.__name, self.__name, x)))
        '''
