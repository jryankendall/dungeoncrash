'''Basic code for mobiles in environments, like creatures.'''


class Entity: 
    '''Generic object representing the player and monsters'''
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy