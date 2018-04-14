'''array manipulation class module'''


import array
from random import randrange


class Board():
    '''array manipulation class'''


    def __init__(self, rows=20, cols=20):
        '''object creation'''
        self.rows = rows
        self.cols = cols
        self.board = array.array('I', [0 for i in range(self.cols*self.rows)])   


    def get_val(self, row, col):
        '''returns value'''
        return self.board[row*self.rows+col]


    def set_val(self, row, col, val):
        '''sets value'''
        self.board[row*self.rows+col] = val


    def is_full(self):
        '''return True if array is full (not contains 0 values)'''
        return 0 not in self.board


    def fill_board(self, val=0):
        '''fills board with value'''
        for i in range(self.cols*self.rows):
            self.board[i] = val

    def set_board(self, data, val=1):
        '''sets board with value according to ...'''
        for row, col in data:
            self.set_val(row,col, val)


    def get_zero_random_pos(self):
        '''return random position with zero value'''
        zeros = [i for i,x in enumerate(self.board) if x==0]
        pos = zeros[randrange(0, len(zeros))]
        return pos//self.cols, pos%self.rows

