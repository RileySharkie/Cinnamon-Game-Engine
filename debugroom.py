import room
from architect import architect
import entities
from camera import Camera


class DebugRoom(room.Room):
    def __init__(self):
        super().__init__()
        self.width = 1600
        self.add_multi(architect('DebugRoom'))
        self.camera = Camera(self.width, self.height, self.get_player())
