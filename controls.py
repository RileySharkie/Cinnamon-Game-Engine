import pygame


class Controls:

    # controls defined
    k_left = pygame.K_LEFT
    k_right = pygame.K_RIGHT
    k_up = pygame.K_UP
    k_down = pygame.K_DOWN
    k_jump = pygame.K_SPACE

    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self. down = False
        self.jump = False
        self.key_dict = {
            self.k_left: 'left',
            self.k_right: 'right',
            self.k_up: 'up',
            self.k_down: 'down',
            self.k_jump: 'jump'
        }

    def key_down(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                setattr(self, control, True)

    def key_up(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                setattr(self, control, False)

