import sys

import pygame

from Game import Game
from Player import Player


def displayBoard(game: Game, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight):
	displayPlayer1(game.player1, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight)
	displayPlayer2(game.player2, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight)


def displayPlayer1(player: Player, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight):
	green = (0, 255, 0)
	blue = (0, 0, 128)
	fontBig = pygame.font.Font('freesansbold.ttf', 32)
	fontSmall = pygame.font.Font('freesansbold.ttf', 20)
	fontVerySmall = pygame.font.Font('freesansbold.ttf', 15)
	nameAndHp = fontBig.render(player.name + "     Life points : " + str(player.HP), True, green, blue)
	graveyard = fontBig.render("Cimetière", True, green, blue)
	deckNb = fontSmall.render("Nb cartes restantes dans le deck :" + str(len(player.deck)), True, green, blue)
	textRect = nameAndHp.get_rect()
	graveyardRect = graveyard.get_rect()
	deckNbRect = deckNb.get_rect()
	textRect.center = (200, 370)
	graveyardRect.center = (screenWidht - 100, 370)
	deckNbRect.center = (600, 370)
	screen.blit(nameAndHp, textRect)
	screen.blit(graveyard, graveyardRect)
	screen.blit(deckNb, deckNbRect)
	player1Monster1 = pygame.Rect(10, 400, cardl, cardL)
	player1Monster2 = pygame.Rect(player1Monster1.x + cardl + 10, 400, cardl, cardL)
	player1Monster3 = pygame.Rect(player1Monster2.x + cardl + 10, 400, cardl, cardL)
	player1Monster4 = pygame.Rect(player1Monster3.x + cardl + 10, 400, cardl, cardL)
	player1Monster5 = pygame.Rect(player1Monster4.x + cardl + 10, 400, cardl, cardL)
	player1GraveYard = pygame.Rect(player1Monster5.x + cardl + 10, 400, cardl, cardL)
	pygame.draw.rect(screen, color, player1Monster1)
	pygame.draw.rect(screen, color, player1Monster2)
	pygame.draw.rect(screen, color, player1Monster3)
	pygame.draw.rect(screen, color, player1Monster4)
	pygame.draw.rect(screen, color, player1Monster5)
	pygame.draw.rect(screen, color, player1GraveYard)
	i = len(player.board)
	if i > 0:
		screen.blit(player.board[0].image, player1Monster1)
		monster1Atk = fontVerySmall.render("Atk :" + str(player.board[0].attack), True, green, blue)
		monster1Def = fontVerySmall.render("Def :" + str(player.board[0].defence), True, green, blue)
		monster1atkRect = monster1Atk.get_rect()
		monster1defRect = monster1Def.get_rect()
		monster1atkRect.center = (70, 680)
		monster1defRect.center = (170, 680)
		screen.blit(monster1Atk, monster1atkRect)
		screen.blit(monster1Def, monster1defRect)
	else:
		screen.blit(backCard, player1Monster1)
	if i > 1:
		screen.blit(player.board[1].image, player1Monster2)
		monster2Atk = fontVerySmall.render("Atk :" + str(player.board[1].attack), True, green, blue)
		monster2Def = fontVerySmall.render("Def :" + str(player.board[1].defence), True, green, blue)
		monster2atkRect = monster2Atk.get_rect()
		monster2defRect = monster2Def.get_rect()
		monster2atkRect.center = (monster1atkRect.x + cardl + 50, 680)
		monster2defRect.center = (monster1defRect.x + cardl + 50, 680)
		screen.blit(monster2Atk, monster2atkRect)
		screen.blit(monster2Def, monster2defRect)
	else:
		screen.blit(backCard, player1Monster2)
	if i > 2:
		screen.blit(player.board[2].image, player1Monster3)
		monster3Atk = fontVerySmall.render("Atk :" + str(player.board[2].attack), True, green, blue)
		monster3Def = fontVerySmall.render("Def :" + str(player.board[2].defence), True, green, blue)
		monster3atkRect = monster3Atk.get_rect()
		monster3defRect = monster3Def.get_rect()
		monster3atkRect.center = (monster2atkRect.x + cardl + 50, 680)
		monster3defRect.center = (monster2defRect.x + cardl + 50, 680)
		screen.blit(monster3Atk, monster3atkRect)
		screen.blit(monster3Def, monster3defRect)
	else:
		screen.blit(backCard, player1Monster3)
	if i > 3:
		screen.blit(player.board[3].image, player1Monster4)
		monster4Atk = fontVerySmall.render("Atk :" + str(player.board[3].attack), True, green, blue)
		monster4Def = fontVerySmall.render("Def :" + str(player.board[3].defence), True, green, blue)
		monster4atkRect = monster4Atk.get_rect()
		monster4defRect = monster4Def.get_rect()
		monster4atkRect.center = (monster3atkRect.x + cardl + 50, 680)
		monster4defRect.center = (monster3defRect.x + cardl + 50, 680)
		screen.blit(monster4Atk, monster4atkRect)
		screen.blit(monster4Def, monster4defRect)

	else:
		screen.blit(backCard, player1Monster4)
	if i > 4:
		screen.blit(player.board[4].image, player1Monster5)
		monster5Atk = fontVerySmall.render("Atk :" + str(player.board[4].attack), True, green, blue)
		monster5Def = fontVerySmall.render("Def :" + str(player.board[4].defence), True, green, blue)
		monster5atkRect = monster5Atk.get_rect()
		monster5defRect = monster5Def.get_rect()
		monster5atkRect.center = (monster4atkRect.x + cardl + 50, 680)
		monster5defRect.center = (monster4defRect.x + cardl + 50, 680)
		screen.blit(monster4Atk, monster5atkRect)
		screen.blit(monster4Def, monster5defRect)
	else:
		screen.blit(backCard, player1Monster5)
	if len(player.defause) > 0:
		screen.blit(player.defause[-1].image, player1GraveYard)
	else:
		screen.blit(backCard, player1GraveYard)


def displayPlayer2(player, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight):
	green = (0, 255, 0)
	blue = (0, 0, 128)
	oui = pygame.font.Font('freesansbold.ttf', 32)
	fontSmall = pygame.font.Font('freesansbold.ttf', 20)
	fontVerySmall = pygame.font.Font('freesansbold.ttf', 15)
	nameAndHp = oui.render(player.name + "     Life points : " + str(player.HP), True, green, blue)
	graveyard = oui.render("Cimetière", True, green, blue)
	deckNb = fontSmall.render("Nb cartes restantes dans le deck :" + str(len(player.deck)), True, green, blue)
	textRect = nameAndHp.get_rect()
	graveyardRect = graveyard.get_rect()
	deckNbRect = deckNb.get_rect()
	textRect.center = (200, 20)
	graveyardRect.center = (screenWidht - 100, 20)
	deckNbRect.center = (600, 20)
	screen.blit(nameAndHp, textRect)
	screen.blit(graveyard, graveyardRect)
	screen.blit(deckNb, deckNbRect)
	player2Monster1 = pygame.Rect(10, 40, cardl, cardL)
	player2Monster2 = pygame.Rect(player2Monster1.x + cardl + 10, 40, cardl, cardL)
	player2Monster3 = pygame.Rect(player2Monster2.x + cardl + 10, 40, cardl, cardL)
	player2Monster4 = pygame.Rect(player2Monster3.x + cardl + 10, 40, cardl, cardL)
	player2Monster5 = pygame.Rect(player2Monster4.x + cardl + 10, 40, cardl, cardL)
	player2GraveYard = pygame.Rect(player2Monster5.x + cardl + 10, 40, cardl, cardL)
	pygame.draw.rect(screen, color, player2Monster1)
	pygame.draw.rect(screen, color, player2Monster2)
	pygame.draw.rect(screen, color, player2Monster3)
	pygame.draw.rect(screen, color, player2Monster4)
	pygame.draw.rect(screen, color, player2Monster5)
	pygame.draw.rect(screen, color, player2GraveYard)
	i = len(player.board)
	if i > 0:
		screen.blit(player.board[0].image, player2Monster1)
		monster1Atk = fontVerySmall.render("Atk :" + str(player.board[0].attack), True, green, blue)
		monster1Def = fontVerySmall.render("Def :" + str(player.board[0].defence), True, green, blue)
		monster1atkRect = monster1Atk.get_rect()
		monster1defRect = monster1Def.get_rect()
		monster1atkRect.center = (70, 320)
		monster1defRect.center = (170, 320)
		screen.blit(monster1Atk, monster1atkRect)
		screen.blit(monster1Def, monster1defRect)
	else:
		screen.blit(backCard, player2Monster1)
	if i > 1:
		screen.blit(player.board[1].image, player2Monster2)
		monster2Atk = fontVerySmall.render("Atk :" + str(player.board[1].attack), True, green, blue)
		monster2Def = fontVerySmall.render("Def :" + str(player.board[1].defence), True, green, blue)
		monster2atkRect = monster2Atk.get_rect()
		monster2defRect = monster2Def.get_rect()
		monster2atkRect.center = (monster1atkRect.x + cardl + 50, 320)
		monster2defRect.center = (monster1defRect.x + cardl + 50, 320)
		screen.blit(monster2Atk, monster2atkRect)
		screen.blit(monster2Def, monster2defRect)
	else:
		screen.blit(backCard, player2Monster2)
	if i > 2:
		screen.blit(player.board[2].image, player2Monster3)
		monster3Atk = fontVerySmall.render("Atk :" + str(player.board[2].attack), True, green, blue)
		monster3Def = fontVerySmall.render("Def :" + str(player.board[2].defence), True, green, blue)
		monster3atkRect = monster3Atk.get_rect()
		monster3defRect = monster3Def.get_rect()
		monster3atkRect.center = (monster2atkRect.x + cardl + 50, 320)
		monster3defRect.center = (monster2defRect.x + cardl + 50, 320)
		screen.blit(monster3Atk, monster3atkRect)
		screen.blit(monster3Def, monster3defRect)
	else:
		screen.blit(backCard, player2Monster3)
	if i > 3:
		screen.blit(player.board[3].image, player2Monster4)
		monster4Atk = fontVerySmall.render("Atk :" + str(player.board[3].attack), True, green, blue)
		monster4Def = fontVerySmall.render("Def :" + str(player.board[3].defence), True, green, blue)
		monster4atkRect = monster4Atk.get_rect()
		monster4defRect = monster4Def.get_rect()
		monster4atkRect.center = (monster3atkRect.x + cardl + 50, 320)
		monster4defRect.center = (monster3defRect.x + cardl + 50, 320)
		screen.blit(monster4Atk, monster4atkRect)
		screen.blit(monster4Def, monster4defRect)
	else:
		screen.blit(backCard, player2Monster4)
	if i > 4:
		screen.blit(player.board[4].image, player2Monster5)
		monster5Atk = fontVerySmall.render("Atk :" + str(player.board[4].attack), True, green, blue)
		monster5Def = fontVerySmall.render("Def :" + str(player.board[4].defence), True, green, blue)
		monster5atkRect = monster5Atk.get_rect()
		monster5defRect = monster5Def.get_rect()
		monster5atkRect.center = (monster4atkRect.x + cardl + 50, 320)
		monster5defRect.center = (monster4defRect.x + cardl + 50, 320)
		screen.blit(monster4Atk, monster5atkRect)
		screen.blit(monster4Def, monster5defRect)
	else:
		screen.blit(backCard, player2Monster5)
	if len(player.defause) > 0:
		screen.blit(player.defause[-1].image, player2GraveYard)
	else:
		screen.blit(backCard, player2GraveYard)


def display(game):
	backCard = pygame.image.load("pyGame/backCard.png")
	cardl = 225
	cardL = 300
	padding = 10
	nbCartesLigne = 6
	nbCartesColonne = 2
	backCard = pygame.transform.scale(backCard, (cardl, cardL))
	screenWidht = 1500
	screenHeight = cardL * 2 + (nbCartesColonne + 1)*padding + 100
	print(screenHeight)
	mapSize = width, height = screenWidht, screenHeight

	black = 0, 0, 0
	color = (255, 0, 0)
	screen = pygame.display.set_mode(mapSize)
	displayBoard(game, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight)
	screen.fill(black)
	displayBoard(game, backCard, mapSize, black, color, screen, cardl, cardL, screenWidht, screenHeight)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			# clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
			print(pos)
	pygame.display.flip()


def seeCard(card):
	while 1 :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		color = (255, 0, 0)
		mapSize = width, height = 300, 450
		screen = pygame.display.set_mode(mapSize)
		cardSpace = pygame.Rect(20, 20, 150, 200)
		pygame.draw.rect(screen, color, cardSpace)
		screen.blit(card.image, cardSpace)