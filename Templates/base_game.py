import pygame,sys

WIDTH = 240
HEIGHT = 360
FPS = 60
TITLE = "Base Pygame"
BK = (0,0,0)

pygame.init()
pygame.mixer.init()
screen  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

running = True
while running:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #UPDATE

    #Fill the screen in black
    screen.fill(BK)
    all_sprites.draw(screen)
    #flips display after everything is initialised
    pygame.display.flip()

class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(WIDTH,HEIGHT)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        pass
    def update(self):
        pass
    def draw(self):
        self.screen.fill(BK)
        self.all_sprites.draw(self.screen)
        pygame.display.fli()
