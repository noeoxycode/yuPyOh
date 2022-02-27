import pygame

class Card:
	def __init__(self, name, types, effect, effectInt, image):
		self.name = name
		self.types = types
		self.effect = effect
		self.effectInt = effectInt
		self.image = pygame.image.load("image/" + image + "png")
		self.holder = None


