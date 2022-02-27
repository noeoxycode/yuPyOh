import pygame

class Card:
	def __init__(self, name, types, effect, effectInt):
		self.name = name
		self.types = types
		self.effect = effect
		self.effectInt = effectInt
		self.image = pygame.image.load("image/" + name + ".png")
		self.image = pygame.transform.scale(self.image, (150, 200))
		self.holder = None


