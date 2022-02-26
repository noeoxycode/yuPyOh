import pygame

class Card:
    def __init__(self, x, y, img):
        self.coords = [x, y]
        self.img = pygame.image.load(img)
