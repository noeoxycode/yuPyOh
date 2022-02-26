import sys, pygame

import sprites as sprites

pygame.init()

mapSize = width, height = 970, 800
speed = [8, 1]
black = 0, 0, 0
surface = pygame.display.set_mode((500, 500))

color = (255, 0, 0)

screen = pygame.display.set_mode(mapSize)

backCard = pygame.image.load("backCard.png")
backCard = pygame.transform.scale(backCard, (150, 200))
#ballrect = backCard.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            print(pos)

    screen.fill(black)
    y = 10

    for cptPart in range(2):
        x = 10
        for cptCard in range(6):
            cardSpace = pygame.Rect(x, y, 150, 200)
            pygame.draw.rect(surface, color, cardSpace)
            screen.blit(backCard, cardSpace)
            x = x + 160
        y = y + 210

    #screen.blit(ball, rectan)
    pygame.display.flip()