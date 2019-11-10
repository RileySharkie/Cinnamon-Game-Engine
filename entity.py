

class Entity:
    visible = True
    live = False
    location = (0, 0)
    spriteList = []
    current_sprite = None
    try_move = 0

    def __init__(self, loc):
        self.location = loc



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
