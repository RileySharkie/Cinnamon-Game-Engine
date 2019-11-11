import room
from architect import architect
import entities


class DebugRoom(room.Room):
    def __init__(self):
        super().__init__()
        self.add_multi(architect('DebugRoom'))