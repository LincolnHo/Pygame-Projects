import pygame,sys
from settings import *
import Player,util,Platform


class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        # load sprite sheets
        self.loadSprite()



        self.new()
        self.running = True

    def makeGround(self):
        for x in range (-35,735,35):
            floor = Platform.Platform(x, HEIGHT - 28,WIDTH/2 - 14, 28,self)
            self.platform_sprites.add(floor)
            self.all_sprites.add(floor)

    def loadSprite(self):
        self.u = util.Util()
        self.spriteSheet = self.u.returnImage(SPRITE_SHEET)
        self.tileSheet = self.u.returnImage(TILE_SHEET)
        self.moonSheet = self.u.returnImage(MOON_SHEET)
        self.cloudSheet = self.u.returnImage(CLOUD_SHEET)
        self.clouds = pygame.transform.scale2x(self.u.blitImage(self.cloudSheet,0,12,74,13))
        self.clouds.set_colorkey((0,0,0))
        self.fullMoon = pygame.transform.smoothscale(self.u.blitImage(self.moonSheet,42,2,22,30),(44,60))
        self.fullMoon.set_colorkey((0,0,0))

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platform_sprites = pygame.sprite.Group()


        self.player = Player.Player(self)
        self.makeGround()

        self.all_sprites.add(self.player)
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jumpCut()
    def update(self):

        hits = pygame.sprite.spritecollide(self.player,self.platform_sprites,False)
        if self.player.vel.y > 0:

            if hits and self.player.pos.y < hits[0].rect.bottom:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                self.player.jumping = False

        self.all_sprites.update()

        if self.player.rect.left > WIDTH * 0.6:
            for p in self.platform_sprites:
                p.rect.x -= self.player.vel.x
        if self.player.rect.left < WIDTH * 0.4:
            for p in self.platform_sprites:
                p.rect.x += -self.player.vel.x

        for p in self.platform_sprites:
            if p.rect.right < 0:
                p.rect.left = WIDTH
            if p.rect.left > WIDTH:
                p.rect.right = 0
    def draw(self):
        self.screen.fill((67,113,198))
        #self.screen.blit(self.fullMoon, (WIDTH * 0.75, HEIGHT - 88))

        self.screen.blit(self.clouds, (200,120))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()

while g.running:
    g.run()
    g.show_go_screen()

pygame.quit()
