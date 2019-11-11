

class Entity:
    visible = True
    live = False
    location = (0, 0)
    spriteList = []
    current_sprite = None
    try_move = 0
    width = 0
    height = 0

    def __init__(self, loc):
        self.location = loc
        self.solid = False

    def get_sprites(self):
        return self.spriteList

    def get_bounds(self):
        #returns the left, top, right, bottom bounds, in that order
        x, y = self.location
        return x, y, x + self.width, y + self.height

    def is_visible(self):
        return self.visible

    def is_live(self):
        return self.live

    def is_solid(self):
        return self.solid

    def get_current_sprite(self):
        return self.current_sprite

    def get_location(self):
        return self.location

    def action(self, entity_list):
        pass
    # this class is inherited. it will be called each frame only if the entity is living

    def move(self, entity_list, destination, check_for):
        # establish start location and desired end location
        startx, starty = self.location
        destx, desty = destination
        # determine if a change in x or y is being attempted and if it will be positive or negative
        if startx < destx:
            xmod = 1
        elif startx > destx:
            xmod = -1
        else:
            xmod = 0
        if starty < desty:
            ymod = 1
        elif starty > desty:
            ymod = -1
        else:
            ymod = 0

        # these variables will hold the ultimate change in x and y position
        final_x = startx
        final_y = starty

        # for each x and y, check if a change is being attempted
        # iterate through changes in x and y until a collision is found or the end is hit
        # the final changes are determined
        if xmod != 0:
            for x in range(1, abs(startx - destx) + 1):
                if not self.collision_var(entity_list, (startx + (x * xmod), starty), check_for):
                    final_x = startx + (x * xmod)
                else:
                    # if a collision occurs, break the loop. we should look no further
                    break
        if ymod != 0:
            for y in range(1, abs(starty - desty) + 1):
                if not self.collision_var(entity_list, (final_x, starty + (y * ymod)), check_for):
                    final_y = starty + (y * ymod)
                else:
                    break
        # the new x,y location is returned
        return final_x, final_y

    def collision_var(self, entity_list, check_location, check_for):
        # this checks if any entities in the entity_list, meeting the parameter criteria of check_for, are found at the
        # given location. returns false if no collision is found, true if otherwise
        lbound, tbound = check_location
        x, y = check_location
        rbound, bbound = x + self.width, y + self.height
        for item in entity_list:
            if item == self:
                continue
            if getattr(item, check_for):  # check to see if the item meets the criteria
                if self.collision((lbound, tbound, rbound, bbound), item.get_bounds()):
                    return True
        # none of the items returned a collision. there were no collisions. return false to indicate this
        return False

    def collision_type(self, entity_list, check_location, type):
        # this checks if any entities in the entity_list, being the same type as indicated, are found at the
        # given location. returns false if no collision is found, true if otherwise
        lbound, tbound = check_location
        x, y = check_location
        rbound, bbound = x + self.width, y + self.height
        for item in entity_list:
            if type(item) == type:  # check to see if the item is the desired type
                if self.collision((lbound, tbound, rbound, bbound), item.get_bounds()):
                    return True
        # none of the items returned a collision. there were no collisions. return false to indicate this
        return False

    @staticmethod
    def collision(check_bounds, target_bounds):
        # the actual collision checking happens here. this method can be static since there are no self references
        lbound, tbound, rbound, bbound = check_bounds
        left, top, right, bottom = target_bounds
        # if any of these conditions are met, then the bounds could not possibly be collising with the
        # target item
        if rbound > left and bbound > top and lbound < right and tbound < bottom:
            return True
        # if none of these statements were true, then a collision must be present. return false
        # this item did not return a collision. return false to indicate this
        return False
