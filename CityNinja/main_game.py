import pygame,random, sprites
from settings import *
from sprites import *


class Game():
    def __init__(self):
        #initialise windows
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()


        #initialise bg image
        self.bg = pygame.image.load(BG_IMAGE)
        self.bg_rect = self.bg.get_rect()

        #store platform tiles
        self.pTile = pygame.image.load(PLATFORM_IMG)
        #initialise title music


        self.running = True
    def new(self):
        #initialise game e.g. starting a new game
        self.Score = -1

        #initialise bg music
        pygame.mixer.music.load(BG_MUSIC)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        #initilise sprites
        self.all_sprites = pygame.sprite.Group()
        self.platform_sprites = pygame.sprite.Group()
        self.player = sprites.Player(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player.headBand)


        for plat in PLATFORM_LIST:
            p = Platform(*plat, self.pTile)
            self.platform_sprites.add(p)
            self.all_sprites.add(p)


        self.run()

    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop - updates
        self.all_sprites.update()

        #player collision when falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player,self.platform_sprites,False)
            if hits and self.player.pos.y < hits[0].rect.bottom:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        #prevent players from forever accelerating && deleting platforms that are out of sight
        if self.player.rect.top < HEIGHT / 3:
            self.player.pos.y += max(2,abs(self.player.vel.y))
            for p in self.platform_sprites:
                p.rect.y += abs(self.player.vel.y)
                if p.rect.top >= HEIGHT:
                    p.kill()
                    self.Score += 1

        #spawn new platforms

        while len(self.platform_sprites) < MAX_PLATFORM:
            w = random.randint(70,100)
            x = random.randint(40,WIDTH-w-40)
            y = random.randint(-160, -80)
            p = sprites.Platform(x,y,w,15,self.pTile)
            self.platform_sprites.add(p)
            self.all_sprites.add(p)

        #tape headBand and maintain sprite integrity
        if self.player.facingRight:
            self.player.headBand.rect.y = self.player.rect.y - 10
            self.player.headBand.rect.x = self.player.rect.x - 9
        else:
            self.player.headBand.rect.y = self.player.rect.y - 10
            self.player.headBand.rect.x = self.player.rect.x - 1


        #kill any sprite that falls beneath sight
        if self.player.rect.bottom > HEIGHT:
            for s in self.all_sprites:
                s.rect.y -= max(self.player.vel.y, 8)
                if s.rect.bottom < 0:
                    s.kill()

        if len(self.platform_sprites) == 0: self.playing = False
    def events(self):
        #game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing: self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        #game loop - drawing
        self.screen.fill(BLACK)
        self.screen.blit(self.bg,self.bg_rect)
        self.all_sprites.draw(self.screen)
        #flips display after everything is initialised
        pygame.display.flip()


    def show_start_screen(self):
        self.screen.blit(self.bg,self.bg_rect)
        self.draw_text(TITLE,40,WHITE,WIDTH/2, 40)
        self.draw_text('A and D to move, Space to Jump', 25, WHITE, WIDTH/2,HEIGHT/2)
        self.draw_text('Press any key to continue', 20, WHITE, WIDTH/2,HEIGHT/2 + 50)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running: return
        self.screen.blit(self.bg,self.bg_rect)
        self.draw_text('GAME OVER',40,WHITE,WIDTH/2, 40)
        self.draw_text('Final Score: ' + str(self.Score),20,WHITE,WIDTH/2, HEIGHT/2)
        self.draw_text('Press any key to play again', 20, WHITE, WIDTH/2,HEIGHT/2 + 50)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

    def draw_text(self,text,size,colour,x,y):
        font = pygame.font.SysFont(GAME_FONT, size)
        text_surface = font.render(text,True,colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


g = Game()
g.show_start_screen()



while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()
