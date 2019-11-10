import pygame as pg
import room as r
import entity


def architect(room):
    grid = 32
    with open('assets/rooms/' + room + '.txt', 'r') as file:
        data = file.read().replace('\n', '')
    for line in data:
        line = line.split(' ')
    entity_list = []
    xpos, ypos = 0, 0
    for line in data:

        for entry in line:
            if entry != 0:
                entity_list.append((entry, (xpos, ypos)))
            xpos += grid
        xpos = 0
        ypos += grid
    return entity_list

