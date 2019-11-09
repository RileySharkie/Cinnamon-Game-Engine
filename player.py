import entity


class Player(entity.Entity):

    def __init__(self):
        super().__init__()
        self.spriteList.append('player')
        self.current_sprite = 'player'
        self.live = True

    def action(self, controls):
        self.try_move = 0
        if controls.left == True and controls.right == False:
            self.try_move = -5
        if controls.left == False and controls.right == True:
            self.try_move = 5
        (x, y) = self.location
        self.location = (x + self.try_move, y)
