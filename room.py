import pygame
import sprite
from player import Player


class Room:

    width = 0
    height = 0
    cameraStartX = 0
    cameraStartY = 0
    entityList = []
    spriteList = {}
    room_name = ''
    gravity = 5

    def __init__(self):
        self.width = 800
        self.height = 640
        self.cameraStartX = 0
        self.cameraStartY = 0

    def add_entity(self, entity):
        self.entityList.append(entity)
        if entity.is_visible():
            for item in entity.get_sprites():
                if item not in self.spriteList:
                    self.spriteList[item] = sprite.Sprite('assets/sprites/' + item + '.png')

    def add_multi(self, tile_set):
        for item in tile_set:
            self.add_entity(item)

    def blit(self):
        blit_list = []
        for item in self.entityList:
            if item.is_visible():
                blit_list.append((self.spriteList[item.get_current_sprite()].get(), item.get_location()))
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
