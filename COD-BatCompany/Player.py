import pygame

RED = (255,0,0)
YELLOW = (255,255,0)

class Player(pygame.sprite.Sprite):

    frames = []

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((70,80))
        self.image.set_colorkey((0,0,0))
        image = pygame.image.load('sprite.png')
        self.image.blit(image,(-10,-376))
        self.rect = self.image.get_rect()
        self.rect.height += 1
        self.rect.bottom  = 550
        self.jumpCount = 0
        self.jumpPower = 22
        self.facingRight = True
        self.Sound = pygame.mixer.Sound('fire.wav')


    def jump(self):
        if self.jumpCount == 0:
            self.jumpCount = self.jumpPower
            self.jumpPower = 22

    def shoot(self):

        if self.facingRight:
            x = self.rect.right
        else:
            x = self.rect.left
        self.Sound.play()
        b = Bullet(x, self.rect.centery, self.facingRight)
        return b


    def update(self):
        self.speedx = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_a]:
            self.speedx = -8
            if self.facingRight: self.image = pygame.transform.flip(self.image,True, False)
            self.facingRight = False
        elif key_state[pygame.K_d]:
            self.speedx = 8
            if not self.facingRight: self.image = pygame.transform.flip(self.image,True, False)
            self.facingRight = True
        if key_state[pygame.K_SPACE]:
            self.jumpPower += 1
            if self.jumpPower > 35: self.jumpPower = 35


        if self.jumpCount != 0:
            self.rect.y -= self.jumpCount
            self.jumpCount -= 1



        self.rect.x += self.speedx

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > 800: self.rect.right = 800


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x , centery, direction):
        super(Bullet, self).__init__()
        self.image  = pygame.Surface((30,10))
        self.image.set_colorkey((0,0,0))
        image = pygame.image.load('bullet.png')
        self.image.blit(image,(-63,-186))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = centery
        self.speedx = 20
        if not direction: self.speedx *= -1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > 800 or self.rect.left < 0:
            self.kill()
