'''Wonsz game module'''

from directions import Directions

class Wonsz():
    '''Wonsz class'''

    def __init__(self, board):
        '''object creation'''
        self.directions = Directions()
        self.direction = self.directions.get_random_direction()
        self.board = board
        self.body = [(self.board.rows//2, self.board.cols//2)]
