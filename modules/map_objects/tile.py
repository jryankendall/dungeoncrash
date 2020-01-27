'''Code for tiles'''
class Tile:
    '''A tile on a map.'''
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        #By default. If a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

        self.explored = False
