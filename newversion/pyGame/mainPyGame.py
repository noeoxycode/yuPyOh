import sys, pygame


from Game import Game

pygame.init()

mapSize = width, height = 970, 800
black = 0, 0, 0
x = 10
y = 10
color = (255, 0, 0)
screen = pygame.display.set_mode(mapSize)

backCard = pygame.image.load("pyGame/backCard.png")
backCard = pygame.transform.scale(backCard, (150, 200))


# ballrect = backCard.get_rect()

def displayGame():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				print(pos)

		screen.fill(black)

		for cptCard in range(5):
			cardSpace = pygame.Rect(x, y, 150, 200)
			pygame.draw.rect(screen, color, cardSpace)
			screen.blit(backCard, cardSpace)
			x = x + 160

			# screen.blit(ball, rectan)
			pygame.display.flip()
