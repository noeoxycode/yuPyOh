import pygame

class Card:
	def __init__(self, name, types, effect, effectInt):
		self.name = name
		self.types = types
		self.effect = effect
		self.effectInt = effectInt
		self.image = pygame.image.load("image/" + name + ".png")
		self.holder = None


