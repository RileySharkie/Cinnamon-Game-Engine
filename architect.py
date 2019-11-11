import pygame as pg
import room as r
import entities


def architect(room_name):
    # room_name is the name of the room file
    # grid determines how wide one unit is on the grid being interpreted
    grid = 32
    # the file is parsed line by line, creating a list
    with open('assets/rooms/' + room_name + '.txt', 'r') as file:
        data = file.read()#.replace('\n', '')
        data = data.split('\n')
    # the list is iterated through, making it two dimensional
    i = 0
    while i < len(data):
        data[i] = data[i].split(' ')
        i += 1

    # the data has been parsed. now every item is iterated through. items that are non-0 values are added to the tile
    # list along with their coordinates, which are determined based on  their position in the grid and the grid size
    tile_list = []
    xpos, ypos = 0, 0
    for line in data:
        for entry in line:
            if entry != '0':
                tile_list.append((entry, (xpos, ypos)))
            xpos += grid
        xpos = 0
        ypos += grid

    # a new list is created, this one holding objects that are initialized based on the previously parsed data
    entity_list = []
    for item in tile_list:
        ent, coord = item
        method = getattr(entities, ent)  # this line gets the iterators from the entities file
        entity_list.append(method(coord))  # objects are created and added to the list

    return entity_list  #the list is returned

