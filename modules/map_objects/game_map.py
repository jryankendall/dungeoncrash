'''Map example'''
from modules.map_objects.tile import Tile
from modules.map_objects.rectangle import Rect


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def create_room(self, room):
        for x in range(room.x1 +1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
        
    def make_map(self):
            #Create two rooms
            room1 = Rect(20, 15, 10, 15)
            room2 = Rect(35, 15, 10, 15)

            self.create_room(room1)
            self.create_room(room2)