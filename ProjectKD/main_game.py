import sys,pygame, math

pygame.init()

size = width,height = 800,600
white = 255,255,255
speed = 0
angle = 0
translation = [0,0]
screen = pygame.display.set_mode(size)

head  = pygame.image.load("src/head.png")
head = pygame.transform.smoothscale (head, (35,50))
newhead = head
headrect = head.get_rect()

pygame.key.set_repeat(100, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle -= 2
            if event.key == pygame.K_LEFT:
                angle += 2
            if event.key == pygame.K_UP:
                speed += 2
            if event.key == pygame.K_DOWN:
                speed -= 2
    speed = sorted([-10,speed,+10])[1]
    translation[0] = math.sin(math.radians(angle))
    translation[1] = math.cos(math.radians(angle))
    newhead = pygame.transform.rotate(head, angle)
    headrect = headrect.move(speed * translation[0],speed * translation[1])
    if headrect.left < 0:headrect.left = 0
    if headrect.right > width:headrect.right = width
    if headrect.top < 0:headrect.top = 0
    if headrect.bottom > height:headrect.bottom = height

    screen.fill(white)
    screen.blit(newhead, headrect)
    pygame.display.flip()
