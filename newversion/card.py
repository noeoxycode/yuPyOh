import pygame

class Card:
	def __init__(self, x, y, name, types, effect, effectInt):
		self.x = x
		self.y = y
		self.name = name
		self.types = types
		self.effect = effect
		self.effectInt = effectInt
		self.image = ''
		self.holder = ''
	def __init__(self, name, types, effect, effectInt, image, holder):
		self.name = name
		self.types = types
		self.effect = effect
		if type(effectInt) is type([]):
			self.effectInt = effectInt
		else:
			self.effectInt = effectInt.split(" ")
		self.image = pygame.image.load(image)
		self.holder = holder


