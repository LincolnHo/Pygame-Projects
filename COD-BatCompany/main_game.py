import sys,pygame,random
import Player, Platform,Mob

BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 600
def main():
    pygame.init()
    pygame.display.set_caption("Call of Duty - Bat Company")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))


    score = 0
    health = 100


    bg = pygame.image.load('bg.png').convert()
    bg_rect = bg.get_rect()

    pygame.mixer.pre_init()

    pygame.mixer.music.load('bg.wav')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    mytext = pygame.font.SysFont('monospace',50)
    pygame.key.set_repeat(50,200)


    hurt = pygame.mixer.Sound('hurt.wav')
    hurt.set_volume(0.2)

    jump = pygame.mixer.Sound('jump.wav')
    jump.set_volume(0.5)

    gameOver = False

    player = Player.Player()
    ground = Platform.Ground(WIDTH,HEIGHT)
    block1 = Platform.Block(450,180)
    block2 = Platform.Block(100,270)
    block3 = Platform.Block(450,360)
    block4 = Platform.Block(100,90)

    platform_sprites = pygame.sprite.Group()
    platform_sprites.add(ground)
    platform_sprites.add(block1)
    platform_sprites.add(block2)
    platform_sprites.add(block3)
    platform_sprites.add(block4)

    bullet_sprites = pygame.sprite.Group()

    mob_sprites = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    m = Mob.Mob(WIDTH,random.randint(200,400))
    mob_sprites.add(m)


    all_sprites.add(ground)
    all_sprites.add(block1)
    all_sprites.add(block2)
    all_sprites.add(block3)
    all_sprites.add(block4)

    all_sprites.add(m)

    all_sprites.add(player)

    while not gameOver:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                b = player.shoot()
                bullet_sprites.add(b)
                all_sprites.add(b)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and pygame.sprite.spritecollide(player,platform_sprites,False):
                player.jump()
                jump.play()
            if event.key == pygame.K_q:
                player.rect.x -= 200
            if event.key == pygame.K_e:
                player.rect.x += 200

        player.rect.bottom += 10

        hits = pygame.sprite.spritecollide(player,platform_sprites,False)
        if hits and player.jumpCount <= 0:
            if player.rect.bottom < hits[0].rect.bottom:
                player.rect.bottom = hits[0].rect.top + 1


        #if player.rect.top <= 0: player.rect.y = 0

        hits = pygame.sprite.groupcollide(bullet_sprites,mob_sprites,True,True)
        for h in hits:
            while len(mob_sprites.sprites()) < 1+score//10:
                m = Mob.Mob(WIDTH,random.randint(200,400))
                mob_sprites.add(m)
                all_sprites.add(m)
            score += 1

        if pygame.sprite.spritecollide(player,mob_sprites,False):
            health -= 0.5
            hurt.play(0,800)
            if health <= 0:
                gameOver = True
                pygame.time.wait(1500)
                pygame.mixer.quit()

        all_sprites.update()
        screen.fill(BLACK)
        screen.blit(bg,bg_rect)
        screen.blit(printScore(mytext,score, health),(400,10))
        all_sprites.draw(screen)
        pygame.display.flip()


    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        screen.fill(BLACK)
        highScore = 0
        highest = False
        f = open('highScore.txt', 'r')
        line = f.readline()
        if line != '' :highScore = int(line)
        f.close()
        if score > highScore:
            f = open('highScore.txt','w')
            f.write(str(score))
            f.close()
            highest = True
            highScore = score

        label = printDeath(mytext,score)
        screen.blit(label,((WIDTH/2 - label.get_rect().width /2,200)))
        label = congrats(mytext,highScore)
        screen.blit(label,((WIDTH/2 - label.get_rect().width /2,300)))
        pygame.display.flip()



def printScore(mt,s,hp):
    label = mt.render('Score: %d Health: %d' % (s, hp), 1, (255,255,255))
    return label

def printDeath(mt,s):
    mt = pygame.font.SysFont('monospace', 100)
    label = mt.render('Final Score: %d' % s, 1, (255,255,255))
    return label

def congrats(mt,s):
    mt = pygame.font.SysFont('monospace', 60)
    label = mt.render('High Score: %d' % s, 1, (255,255,255))
    return label

if __name__ == '__main__':
    main()
