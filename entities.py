import entity

grid_size = 32

class Block(entity.Entity):
    def __init__(self, loc):
        super().__init__(loc)
        self.live = False
        self.solid = True
        self.visible = True
        self.width = grid_size
        self.height = grid_size


class DarkStone(Block):
    def __init__(self, loc):
        super().__init__(loc)
        self.spriteList.append('darkstone')
        self.set_current_sprite('darkstone')



class Stone(Block):
    def __init__(self, loc):
        super().__init__(loc)
        self.spriteList.append('stone')
        self.set_current_sprite('stone')
