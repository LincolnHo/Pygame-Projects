import sys,pygame
from weapon import Weapon
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    mytext = pygame.font.SysFont('monospace',50)
    black = 0,0,0
    pygame.key.set_repeat(50,50)


    player1 = Player("Lincoln")

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.fire()
            if event.key == pygame.K_r:
                player1.reload()
            if event.key == pygame.K_v:
                player1.melee()
            if event.key == pygame.K_UP:
                player1.movePlayer(0,-1)
            if event.key == pygame.K_DOWN:
                player1.movePlayer(0,1)
            if event.key == pygame.K_LEFT:
                player1.movePlayer(-1,0)
            if event.key == pygame.K_RIGHT:
                player1.movePlayer(1,0)
            if event.key == pygame.K_LSHIFT:
                player1.setSprinting(True)

            if event.key == pygame.K_1:
                player1.changeWeapon(0)
            if event.key == pygame.K_2:
                player1.changeWeapon(1)
            if event.key == pygame.K_3:
                player1.changeWeapon(2)
            if event.key == pygame.K_4:
                player1.changeWeapon(3)
            if event.key == pygame.K_5:
                player1.changeWeapon(4)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1.movePlayer(0,0)
            if event.key == pygame.K_DOWN:
                player1.movePlayer(0,0)
            if event.key == pygame.K_LEFT:
                player1.movePlayer(0,0)
            if event.key == pygame.K_RIGHT:
                player1.movePlayer(0,0)
            if event.key == pygame.K_LSHIFT:
                player1.setSprinting(False)

        player1.sprite.update()
        screen.fill(black)
        drawText(screen,mytext,player1)
        player1.sprite.draw(screen)
        pygame.display.flip()


def drawText(s,mt,p):
    if p.getAmmo() > 0 or p.getBulletInClip() > 0:
        label = mt.render("%d/%d" % (p.getBulletInClip(), p.getAmmo()),1,(255,255,255))
        s.blit(label,(600,550))

if __name__ == '__main__':
    main()
