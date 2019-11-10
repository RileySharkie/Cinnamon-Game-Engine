import entity


class Block(entity.Entity):
    def __init__(self, loc):
        super(entity.Entity, self).__init__(loc)
        self.live = False
        self.visible = True


class DarkStone(Block):
    def __init__(self, loc):
        super(Block, self).__init__(loc)
        self.spriteList.append('darkstone')
        self.current_sprite = 'darkstone'


class Stone(Block):
    def __init__(self, loc):
        super(Block, self).__init__(loc)
        self.spriteList.append('stone')
        self.current_sprite = 'stone'