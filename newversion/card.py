class Card:
	def __init__(self, x, y, name, types, effect, effectInt, image, holder):
		self.x = x
		self.y = y
		self.name = name
		self.types = types
		self.effect = effect
		if type(effectInt) is type([]):
			self.effectInt = effectInt
		else:
			self.effectInt = effectInt.split(" ")
		self.image = image
		self.holder = holder


