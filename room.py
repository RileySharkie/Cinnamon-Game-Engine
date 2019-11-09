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

    def __init__(self):
        self.width = 800
        self.height = 600
        self.cameraStartX = 0
        self.cameraStartY = 0

        self.player = Player()

        self.player2 = Player()
        self.player2.location = (30, 30)
        self.add_entity(self.player)
        self.add_entity(self.player2)

    def add_entity(self, entity):
        self.entityList.append(entity)
        if entity.is_visible():
            for item in entity.get_sprites():
                if item not in self.spriteList:
                    self.spriteList[item] = sprite.Sprite('assets/sprites/' + item + '.png')

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
