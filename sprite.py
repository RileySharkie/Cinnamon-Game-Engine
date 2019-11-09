import pygame


class Sprite:

    def __init__(self, get_string):

        self.sprite = pygame.image.load(get_string)
        self.sprite.set_colorkey((255, 0, 255))

    def get(self):
        return self.sprite
