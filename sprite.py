import pygame


class Sprite:

    frames = 0
    width = 0
    height = 0
    origin = 0, 0
    hitbox = 0, 0, 0, 0  # left, top, right, bottom
    speed = 0  # the speed at which the sprite animates

    def __init__(self, get_string, frames=0, origin=(0, 0), width=0, height=0, hitbox=(0, 0, 0, 0), speed = 2):

        self.sprite = pygame.image.load(get_string)
        self.sprite.set_colorkey((255, 0, 255))

        self.frames = frames

        self.speed = speed

        if width == 0:
            self.width = self.sprite.get_width()
        else:
            self.width = width
        if height == 0:
            self.height = self.sprite.get_height()
        else:
            self.height = width

        self.origin = origin

        if hitbox == (0, 0, 0, 0):
            x, y = origin
            self.hitbox = (x, y, self.width - x, self.height - y)
        else:
            self.hitbox = hitbox

    def get_hitbox(self):
        return self.hitbox

    def get(self):
        return self.sprite

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_frames(self):
        return self.frames

    def get_speed(self):
        return self.speed

    def get_frame(self, frame):
        if frame == -1:
            return 0, 0, self.width, self.height
        else:
            columns = self.sprite.get_width() // self.width
            col = frame % columns
            row = frame // columns
            return col * self.width, row * self.height, self.width, self.height
