import pygame, sys


def load_image(name):
    image = pygame.image.load(name)
    return image

class Player:
    __name = ""
    __hitpoint  = 0
    __handgunAmmo = 0
    __rifleAmmo = 0
    __shotgunAmmo = 0
    __canMelee = True
    __canFire = True
    __moving = False
    __running = False
    __mode = 0;
    def __init__(self, name):
        self.__name = name
        self.__hitpoint = 100
        self.__handgunAmmo = 50
        self.__rifleAmmo = 120
        self.__shotgunAmmo = 40
        self.sprite = PlayerSprite()
        self.changeWeapon(self.__mode)

    def move(self, vertical,horizontal):
        self.sprite.move(5 * horizontal, 5 * vertical)
        self.setMoving(True)

    def fire(self):
        if self.sprite.returnFireCD() < 0 and self.__canFire:
            self.sprite.fireAnim()

    def reload(self):
        if self.sprite.returnReloadCD() < 0 and self.__canFire:
            self.sprite.reloadAnim()

    def setRunning(self,boo):
        self.__running = boo
        self.sprite.running(boo)
    def setMoving(self, boo):
        self.__moving = boo
        self.sprite.moving(boo)

    def melee(self):
        if self.sprite.returnMeleeCD() < 0 and self.__canMelee:
            self.sprite.meleeAnim()

    def changeWeapon(self,weapon):
        self.sprite.changeWeapon(weapon)
        if weapon == 0:
            self.__canFire = False
            self.__canMelee = False
        if weapon == 1:
            self.__canFire = False
            self.__canMelee = True
        if weapon == 2:
            self.__canMelee = True
            self.__canFire = True
        if weapon == 3:
            self.__canMelee = False
            self.__canFire = True
            self.sprite.setNewCD(2,28,28)
        if weapon == 4:
            self.__canMelee = False
            self.__canFire = True
            self.sprite.setNewCD(25,28,28)


class UpperBodySprite(pygame.sprite.Sprite):

    mode = 0
    animCount = 2
    timer = 2
    __firing = False    # 3 frames
    __reload = False    # 3 frames
    __melee = False     # 14 frames
    __moving = False   # 19 frames & 19 more for idle


    def __init__(self):
        super(UpperBodySprite, self).__init__()

        self.FloadingAnim()
        self.KloadingAnim()
        self.HGloadingAnim()
        self.RloadingAnim()
        self.SloadingAnim()

        self.index = 0
        self.weapon = 0
        self.mode = 0
        self.images = [self.Fimages,self.Kimages,self.HGimages,self.Rimages,self.Simages]
        self.image = self.images[self.weapon][self.mode][self.index]
        self.rect = pygame.Rect(5,5,358,353)

    def HGloadingAnim(self):
        self.handIdle = []
        self.handWalk = []
        self.handMelee = []
        self.handFire = []
        self.handReload = []


        for x in range(0,20):
            self.handIdle.append(load_image('Top_Down_Survivor/handgun/idle/survivor-idle_handgun_%d.png' % x))
            self.handWalk.append(load_image('Top_Down_Survivor/handgun/move/survivor-move_handgun_%d.png' % x))
        for x in range(0,15):
            self.handMelee.append(load_image('Top_Down_Survivor/handgun/meleeattack/survivor-meleeattack_handgun_%d.png' % x))
            self.handReload.append(load_image('Top_Down_Survivor/handgun/reload/survivor-reload_handgun_%d.png' % x))
        for x in range (0,3):
            self.handFire.append(load_image('Top_Down_Survivor/handgun/shoot/survivor-shoot_handgun_%d.png' % x))


        self.HGimages = [self.handIdle,self.handWalk,self.handMelee,self.handFire,self.handReload]

    def RloadingAnim(self):
        self.rIdle = []
        self.rWalk = []
        self.rMelee = []
        self.rFire = []
        self.rReload = []
        for x in range(0,20):
            self.rIdle.append(load_image('Top_Down_Survivor/rifle/idle/survivor-idle_rifle_%d.png' % x))
            self.rWalk.append(load_image('Top_Down_Survivor/rifle/move/survivor-move_rifle_%d.png' % x))
            self.rReload.append(load_image('Top_Down_Survivor/rifle/reload/survivor-reload_rifle_%d.png' % x))
        for x in range(0,15):
            self.rMelee.append(load_image('Top_Down_Survivor/rifle/meleeattack/survivor-meleeattack_rifle_%d.png' % x))
        for x in range (0,3):
            self.rFire.append(load_image('Top_Down_Survivor/rifle/shoot/survivor-shoot_rifle_%d.png' % x))


        self.Rimages = [self.rIdle,self.rWalk,self.rMelee,self.rFire,self.rReload]

    def SloadingAnim(self):
        self.sIdle = []
        self.sWalk = []
        self.sMelee = []
        self.sFire = []
        self.sReload = []
        for x in range(0,20):
            self.sIdle.append(load_image('Top_Down_Survivor/shotgun/idle/survivor-idle_shotgun_%d.png' % x))
            self.sWalk.append(load_image('Top_Down_Survivor/shotgun/move/survivor-move_shotgun_%d.png' % x))
            self.sReload.append(load_image('Top_Down_Survivor/shotgun/reload/survivor-reload_shotgun_%d.png' % x))
        for x in range(0,15):
            self.sMelee.append(load_image('Top_Down_Survivor/shotgun/meleeattack/survivor-meleeattack_shotgun_%d.png' % x))
        for x in range (0,3):
            self.sFire.append(load_image('Top_Down_Survivor/shotgun/shoot/survivor-shoot_shotgun_%d.png' % x))


        self.Simages = [self.sIdle,self.sWalk,self.sMelee,self.sFire,self.sReload]

    def FloadingAnim(self):
        self.fIdle = []
        self.fWalk = []
        self.fMelee = []
        self.fFire = []
        self.fReload = []
        for x in range(0,20):
            self.fIdle.append(load_image('Top_Down_Survivor/flashlight/idle/survivor-idle_flashlight_%d.png' % x))
            self.fWalk.append(load_image('Top_Down_Survivor/flashlight/move/survivor-move_flashlight_%d.png' % x))
        for x in range(0,15):
            self.fMelee.append(load_image('Top_Down_Survivor/flashlight/meleeattack/survivor-meleeattack_flashlight_%d.png' % x))


        self.Fimages = [self.fIdle,self.fWalk,self.fMelee,self.fFire,self.fReload]

    def KloadingAnim(self):
        self.kIdle = []
        self.kWalk = []
        self.kMelee = []
        self.kFire = []
        self.kReload = []
        for x in range(0,20):
            self.kIdle.append(load_image('Top_Down_Survivor/knife/idle/survivor-idle_knife_%d.png' % x))
            self.kWalk.append(load_image('Top_Down_Survivor/knife/move/survivor-move_knife_%d.png' % x))
        for x in range(0,15):
            self.kMelee.append(load_image('Top_Down_Survivor/knife/meleeattack/survivor-meleeattack_knife_%d.png' % x))


        self.Kimages = [self.kIdle,self.kWalk,self.kMelee,self.kFire,self.kReload]

    def changeWeapon(self,weapon):
        self.weapon = weapon


    def fire(self):
        self.__firing = True

    def reload(self):
        self.__reload = True

    def melee(self):
        self.__melee = True


    def changeMove(self, boo):
        self.__moving = boo

    def update(self):
        self.animCount -=1
        if self.animCount <= 0:
            self.index += 1

            if self.__melee == True:
                self.mode = 2
                self.index = 0
                self.__melee = False

            if self.__firing == True:
                self.mode = 3
                self.index = 0
                self.__firing = False

            if self.__reload == True:
                self.mode = 4
                self.index = 0
                self.__reload = False


            if self.index >= len(self.images[self.weapon][self.mode]):
                self.index = 0
                self.mode = 0 if self.__moving == False else  1
            self.image = self.images[self.weapon][self.mode][self.index]
            self.animCount = self.timer

class LowerBodySprite(pygame.sprite.Sprite):

    timer  = 2
    animCount = 2

    __moving = False
    __running = False
    def __init__(self):
        super(LowerBodySprite, self).__init__()
        self.walk = []
        self.run = []
        self.idle = load_image('Top_Down_Survivor/feet/idle/survivor-idle_0.png')
        for x in range(0,20):
            self.walk.append(load_image('Top_Down_Survivor/feet/walk/survivor-walk_%d.png' % x))
            self.run.append(load_image('Top_Down_Survivor/feet/run/survivor-run_%d.png' % x))
        self.index = 0
        self.image = self.walk[self.index]
        self.rect = pygame.Rect(30,60,358,353)


    def changeMove(self, m):
        self.__moving = m
    def changeRun(self, r):
        self.__running = r


    def update(self):
        self.animCount -=1
        if self.animCount <= 0:
            self.index += 1
            if self.index >= len(self.walk):
                self.index = 0
            if self.__moving == False :self.image = self.idle
            if self.__moving == True :self.image = self.walk[self.index]
            if self.__moving == True and self.__running == True :self.image = self.run[self.index]
            self.animCount = self.timer

class PlayerSprite(pygame.sprite.Group):

    __fireC = 10
    __reloadC = 28
    __meleeC = 28
    __running = False

    def __init__(self):
        super(PlayerSprite,self).__init__()
        self.ubsprite = UpperBodySprite()
        self.lbsprite = LowerBodySprite()

        self.add(self.lbsprite)
        self.add(self.ubsprite)
        self.__fireCD = 0
        self.__reloadCD = 0
        self.__meleeCD = 0

    def setNewCD(self,fireCD,reloadCD,meleeCD):
        self.__fireC = fireCD
        self.__reloadC = reloadCD
        self.__meleeC = meleeCD

    def returnFireCD(self):
        return self.__fireCD
    def returnReloadCD(self):
        return self.__reloadCD
    def returnMeleeCD(self):
        return self.__meleeCD

    def fireAnim(self):
        self.ubsprite.fire()
        self.__fireCD = self.__fireC
        self.__reloadCD = self.__fireC
        self.__meleeCD = self.__fireC

    def reloadAnim(self):
        self.ubsprite.reload()
        self.__fireCD = self.__reloadC
        self.__reloadCD = self.__reloadC
        self.__meleeCD = self.__reloadC

    def meleeAnim(self):
        self.ubsprite.melee()
        self.__fireCD = self.__meleeC
        self.__reloadCD = self.__meleeC
        self.__meleeCD = self.__meleeC

    def changeWeapon(self,weapon):
        self.ubsprite.changeWeapon(weapon)

    def running(self,boo):
        self.__running = boo
        self.lbsprite.changeRun(boo)
    def moving(self,boo):
        self.ubsprite.changeMove(boo)
        self.lbsprite.changeMove(boo)


    def move(self, x, y):
        if self.__running:
            self.ubsprite.rect.x += 2* x
            self.ubsprite.rect.y += 2*y
            self.lbsprite.rect.x += 2*x
            self.lbsprite.rect.y += 2*y
        self.ubsprite.rect.x += x
        self.ubsprite.rect.y += y
        self.lbsprite.rect.x += x
        self.lbsprite.rect.y += y

    def update(self):
        self.ubsprite.update()
        self.lbsprite.update()
        self.__fireCD -= 1
        self.__reloadCD -= 1
        self.__meleeCD -= 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    black = 0,0,0
    player = Player("Lincoln")
    pygame.key.set_repeat(50,50)
    mytext = pygame.font.SysFont('monospace',50)


    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.fire()
            if event.key == pygame.K_r:
                player.reload()
            if event.key == pygame.K_v:
                player.melee()
            if event.key == pygame.K_LSHIFT:
                player.setRunning(True)
            if event.key == pygame.K_1:
                player.changeWeapon(0)
            if event.key == pygame.K_2:
                player.changeWeapon(1)
            if event.key == pygame.K_3:
                player.changeWeapon(2)
            if event.key == pygame.K_4:
                player.changeWeapon(3)
            if event.key == pygame.K_5:
                player.changeWeapon(4)
            if event.key == pygame.K_UP:
                player.move(-1,0)
            if event.key == pygame.K_DOWN:
                player.move(1,0)
            if event.key == pygame.K_LEFT:
                player.move(0,-1)
            if event.key == pygame.K_RIGHT:
                player.move(0,1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                player.setRunning(False)
            if event.key == pygame.K_UP:
                player.setMoving(False)
            if event.key == pygame.K_DOWN:
                player.setMoving(False)
            if event.key == pygame.K_LEFT:
                player.setMoving(False)
            if event.key == pygame.K_RIGHT:
                player.setMoving(False)
        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        player.sprite.update()
        screen.fill(black)
        player.sprite.draw(screen)
        label = mytext.render("10/120",1,(255,255,255))
        screen.blit(label,(600,550))
        pygame.display.flip()

if __name__ == '__main__':
    main()
