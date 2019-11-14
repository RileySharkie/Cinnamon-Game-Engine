import pygame


class Sprite:

    def __init__(self, get_string):

        self.sprite = pygame.image.load(get_string)
        self.sprite.set_colorkey((255, 0, 255))

    def get(self):
        return self.sprite

    def get_width(self):
        return self.sprite.get_width()

    def get_height(self):
        return self.sprite.get_height()
