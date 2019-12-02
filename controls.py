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
        self.down = False
        self.jump = False
        self.left_press = False
        self.right_press = False
        self.up_press = False
        self.down_press = False
        self.jump_press = False
        self.key_dict = {
            self.k_left: 'left',
            self.k_right: 'right',
            self.k_up: 'up',
            self.k_down: 'down',
            self.k_jump: 'jump'
        }

    def reset(self):  # resets and key presses. this ensures we know what keys were pressed this frame, as opposed to
        # what keys are simply being held this frame
        for key, control in self.key_dict.items():
            setattr(self, control + '_press', False)


    def key_down(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                setattr(self, control, True)
                setattr(self, control + '_press', True)

    def key_up(self, event):
        for key, control in self.key_dict.items():
            if event.key == key:
                setattr(self, control, False)

