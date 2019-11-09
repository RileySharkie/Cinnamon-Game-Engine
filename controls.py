import pygame


class Controls:

    # controls defined
    k_left = pygame.K_LEFT
    k_right = pygame.K_RIGHT

    def __init__(self):
        self.left = False
        self.right = False
        self.key_dict = {
            self.k_left: self.set_left,
            self.k_right: self.set_right

        }

    def set_left(self, bool):
        self.left = bool

    def set_right(self, bool):
        self.right = bool

    def get_key(self, key):
        return self.key_dict[key]

    def key_down(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                control(True)

    def key_up(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                control(False)
