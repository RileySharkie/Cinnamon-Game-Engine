# this is where metadata about sprites and spritesheets is stored
from sprite import Sprite


def get(string):
    return sprites[string]


sprites = {  # spritename, frames=0, origin=(0, 0), width=0, height=0, hitbox=(0, 0, 0, 0)
    "player": Sprite('assets/sprites/Player.png', frames=2, width=37, speed=3),
    "stone": Sprite('assets/sprites/stone.png'),
    "darkstone": Sprite('assets/sprites/darkstone.png')

}

