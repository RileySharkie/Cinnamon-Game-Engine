

class Entity:

    def __init__(self):
        self.visible = True
        self.live = False
        self.location = (0, 0)
        self. spriteList = []
        self.current_sprite = None
        self.try_move = 0



    def get_sprites(self):
        return self.spriteList

    def is_visible(self):
        return self.visible

    def is_live(self):
        return self.live

    def get_current_sprite(self):
        return self.current_sprite

    def get_location(self):
        return self.location
