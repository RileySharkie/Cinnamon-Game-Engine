import entity


class Player(entity.Entity):

    live = True
    visible = True
    width = 73
    height = 56

    def __init__(self, loc):
        super().__init__(loc)
        self.spriteList.append('player')
        self.set_current_sprite('player')
        self.location = loc



    def action(self, entity_list, controls):
        self.is_grounded(entity_list, 'solid')
        try_move_x = 0
        if controls.left and not controls.right:
            try_move_x = -self.move_speed
            self.flip = True
        if not controls.left and controls.right:
            try_move_x = self.move_speed
            self.flip = False
        if self.grounded:
            self.y_speed = 0
            if controls.jump_press:
                self.jump_extend = self.jump_extend_max
                self.y_speed = -self.jump_speed
        else:
            if self.jump_extend > 0:
                self.jump_extend -= 1
            if not controls.jump:
                self.jump_extend = 0
            if self.y_speed < 0:
                if self.hit_head(entity_list, 'solid'):
                    self.jump_extend = 0
            if self.jump_extend == 0:
                self.y_speed += self.gravity
            else:
                self.y_speed += round(self.gravity/2)
            if self.y_speed > self.max_fall_speed:
                self.y_speed = self.max_fall_speed
        try_move_y = self.y_speed

        if try_move_x != 0 or try_move_y != 0:
            (startx, starty) = self.location
            new_location = self.move(entity_list, (startx + try_move_x, starty + try_move_y), 'solid')
            self.location = new_location
