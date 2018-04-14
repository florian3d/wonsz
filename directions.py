'''directions module'''
from random import randint

class Directions():
    '''Direction class'''

    def __init__(self):
        '''creates Directions object'''
        self.directions = ('L', 'R', 'U', 'D')
        self.left = self.directions[0]
        self.right = self.directions[1]
        self.up = self.directions[2]
        self.down = self.directions[3]

    def get_random_direction(self):
        '''returns random direction'''
        return self.directions[randint(0, 3)]
