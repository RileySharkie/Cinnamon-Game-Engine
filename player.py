import entity


class Player(entity.Entity):

    live = True
    width = 40
    height = 56

    def __init__(self, loc):
        super().__init__(loc)
        self.spriteList.append('player')
        self.current_sprite = 'player'
        self.location = loc

    def action(self, entity_list, controls):
        try_move_x = 0
        if controls.left is True and controls.right is False:
            try_move_x = -5
        if controls.left is False and controls.right is True:
            try_move_x = 5
        try_move_y = 0
        if controls.up is True and controls.down is False:
            try_move_y = -5
        if controls.up is False and controls.down is True:
            try_move_y = 5

        if try_move_x != 0 or try_move_y != 0:
            (startx, starty) = self.location
            new_location = self.move(entity_list, (startx + try_move_x, starty + try_move_y), 'solid')
            self.location = new_location
