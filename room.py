import pygame
import sprite
from player import Player
from camera import Camera
import spritemaster


class Room:

    width = 0
    height = 0
    entityList = []
    spriteList = {}
    room_name = ''
    gravity = 5

    def __init__(self):
        self.width = 800
        self.height = 640
        self.player = None
        self.camera = Camera(self.width, self.height)

    def get_player(self):
        return self.player

    def add_entity(self, entity):
        self.entityList.append(entity)
        if type(entity) is Player:
            self.player = entity
        if entity.is_visible():
            for item in entity.get_sprites():
                if item not in self.spriteList:
                    self.spriteList[item] = spritemaster.get(item)
                    # self.spriteList[item] = sprite.Sprite('assets/sprites/' + item + '.png')

    def add_multi(self, tile_set):
        for item in tile_set:
            self.add_entity(item)

    def blit(self):
        camerax, cameray = self.camera.location
        cameraw, camerah = self.camera.width, self.camera.height
        blit_list = []
        for item in self.entityList:
            if item.is_visible():
                curr_sprite = self.spriteList[item.get_current_sprite()]
                frame = item.advance_frame()
                x, y = item.get_location()
                flip = item.flip
                or_x, or_y = curr_sprite.origin  # account for any skew from sprite origin
                if item.flip:
                    or_x = item.width - or_x
                # check to see if the item is visible (if it is in the camera's view)
                if (x + curr_sprite.get_width() - or_x >= camerax or x + or_x <= camerax + cameraw) and (y + curr_sprite.get_height() - or_y >= cameray or y + or_y <= cameray + camerah):
                    blit_list.append((curr_sprite.get(), (x - or_x - camerax, y - or_y - cameray), curr_sprite.get_frame(frame), flip))
        return blit_list

    def get_live(self):
        live_list = []
        for item in self.entityList:
            if item.is_live():
                live_list.append(item)
        return live_list

    # iterate through the entity list. live entities are called
    # this will allow objects to take any actions that they might take
    # this includes player inputs
    def check_action(self, controls):
        for item in self.get_live():
            if type(item) is Player:
                item.action(self.entityList, controls)
            else:
                item.action(self.entityList)
