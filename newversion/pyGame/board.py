import sys

import pygame

from Game import Game
from Player import Player




def displayBoard(game: Game,backCard,mapSize,black,surface,color,screen):
	displayPlayer1(game.player1,backCard,mapSize,black,surface,color,screen)
	displayPlayer2(game.player2,backCard,mapSize,black,surface,color,screen)


def displayPlayer1(player: Player,backCard,mapSize,black,surface,color,screen):
	player1Monster1 = pygame.Rect(10, 10, 150, 200)
	player1Monster2 = pygame.Rect(170, 10, 150, 200)
	player1Monster3 = pygame.Rect(330, 10, 150, 200)
	player1Monster4 = pygame.Rect(490, 10, 150, 200)
	player1Monster5 = pygame.Rect(650, 10, 150, 200)
	player1GraveYard = pygame.Rect(810, 10, 150, 200)
	pygame.draw.rect(screen, color, player1Monster1)
	pygame.draw.rect(screen, color, player1Monster2)
	pygame.draw.rect(screen, color, player1Monster3)
	pygame.draw.rect(screen, color, player1Monster4)
	pygame.draw.rect(screen, color, player1Monster5)
	pygame.draw.rect(screen, color, player1GraveYard)
	i=len(player.board)
	if i>0:
		screen.blit(player.board[0].image, player1Monster1)
	else:
		screen.blit(backCard, player1Monster1)
	if i>1:
		screen.blit(player.board[1].image, player1Monster2)
	else:
		screen.blit(backCard, player1Monster2)
	if i>2:
		screen.blit(player.board[2].image, player1Monster3)
	else:
		screen.blit(backCard, player1Monster3)
	if i>3:
		screen.blit(player.board[3].image , player1Monster4)
	else:
		screen.blit(backCard, player1Monster4)
	if i>4:
		screen.blit(player.board[4].image , player1Monster5)
	else:
		screen.blit(backCard, player1Monster5)
	if len(player.defause)>0:
		screen.blit(player.defause[-1].image , player1GraveYard)
	else:
		screen.blit(backCard, player1GraveYard)


def displayPlayer2(player,backCard,mapSize,black,surface,color,screen):
	player2Monster1 = pygame.Rect(10, 220, 150, 200)
	player2Monster2 = pygame.Rect(170, 220, 150, 200)
	player2Monster3 = pygame.Rect(330, 220, 150, 200)
	player2Monster4 = pygame.Rect(490, 220, 150, 200)
	player2Monster5 = pygame.Rect(650, 220, 150, 200)
	player2GraveYard = pygame.Rect(810, 220, 150, 200)
	pygame.draw.rect(screen, color, player2Monster1)
	pygame.draw.rect(screen, color, player2Monster2)
	pygame.draw.rect(screen, color, player2Monster3)
	pygame.draw.rect(screen, color, player2Monster4)
	pygame.draw.rect(screen, color, player2Monster5)
	pygame.draw.rect(screen, color, player2GraveYard)
	i=len(player.board)
	if i>0:
		screen.blit(player.board[0].image, player2Monster1)
	else:
		screen.blit(backCard, player2Monster1)
	if i>1:
		screen.blit(player.board[1].image, player2Monster2)
	else:
		screen.blit(backCard, player2Monster2)
	if i>2:
		screen.blit(player.board[2].image, player2Monster3)
	else:
		screen.blit(backCard, player2Monster3)
	if i>3:
		screen.blit(player.board[3].image, player2Monster4)
	else:
		screen.blit(backCard, player2Monster4)
	if i>4:
		screen.blit(player.board[4].image, player2Monster5)
	else:
		screen.blit(backCard, player2Monster5)
	if len(player.defause)>0:
		screen.blit(player.defause[-1].image, player2GraveYard)
	else:
		screen.blit(backCard, player2GraveYard)

def display(game):
	backCard = pygame.image.load("pyGame/backCard.png")
	backCard = pygame.transform.scale(backCard, (150, 200))	
	mapSize = width, height = 700, 600
	black = 0, 0, 0
	surface = pygame.display.set_mode((500, 500))
	color = (255, 0, 0)
	screen = pygame.display.set_mode(mapSize)
	print("toto")
	displayBoard(game,backCard,mapSize,black,surface,color,screen)
	while 1:
		screen.fill(black)
		displayBoard(game,backCard,mapSize,black,surface,color,screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				# clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
				print(pos)
		turn
		pygame.display.flip()

