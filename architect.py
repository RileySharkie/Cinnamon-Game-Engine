import pygame as pg
import room as r
import entities


def architect(room):
    grid = 32
    with open('assets/rooms/' + room + '.txt', 'r') as file:
        data = file.read()#.replace('\n', '')
        data = data.split('\n')
    i = 0
    while i < len(data):
        data[i] = data[i].split(' ')
        i += 1
    tile_list = []
    xpos, ypos = 0, 0
    for line in data:
        for entry in line:
            if entry != '0':
                tile_list.append((entry, (xpos, ypos)))
            xpos += grid
        xpos = 0
        ypos += grid

    print(tile_list)

    entity_list = []
    for item in tile_list:
        ent, coord = item
        method = getattr(entities, ent)
        entity_list.append(method(coord))

    return entity_list

