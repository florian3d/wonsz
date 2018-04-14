from board import Board
from wonsz import Wonsz
from time import time

class Game():

    def __init__(self, rows=20, cols=20):

        self.board = Board(rows=rows, cols=cols)
        self.game_over = False
        self.score = 0
        self.high_score = 0
        self.wonsz = Wonsz(self.board)
        self.apple = self.give_me_apple()
        self.speed = .001
        self.time = time()
        self.eat = False
        self.pause = False


    def restart(self):

        self.board = Board()
        self.game_over = False
        self.won = False
        self.score = 0
        self.wonsz = Wonsz(self.board)
        self.apple = (10, 10)
        self.time = time()
        self.eat = False

    def left(self):

        self.wonsz.direction = self.wonsz.directions.left
        
    def right(self):

        self.wonsz.direction = self.wonsz.directions.right
        
    def up(self):

        self.wonsz.direction = self.wonsz.directions.up
        
    def down(self):

        self.wonsz.direction = self.wonsz.directions.down

    def update(self):
        if not self.pause:
            t0 = time()
            t = (t0-self.time)/100
            if t > self.speed:
                self.time = t0
                self._update_()

    def _update_(self):

        row, col = self.wonsz.body[0]

        if self.wonsz.direction == self.wonsz.directions.left:
            col -= 1
            if col < 0:
                col = 0
        
        if self.wonsz.direction == self.wonsz.directions.right:
            col += 1
            if col >= self.board.cols:
                col = self.board.cols - 1
        
        if self.wonsz.direction == self.wonsz.directions.up:
            row -= 1
            if row < 0:
                row = 0

        if self.wonsz.direction == self.wonsz.directions.down:
            row += 1
            if row >= self.board.rows:
                row = self.board.rows - 1

        if (row, col) in self.wonsz.body:
            self.game_over = True

        else:
            if self.wonsz.body[0] == self.apple:
                self.score += len(self.wonsz.body)
                if self.score > self.high_score:
                    self.high_score = self.score
                self.eat = True
                self.apple = self.give_me_apple()

            self.wonsz.body.insert(0, (row, col))
            if not self.eat:
                self.wonsz.body.pop()
            self.eat = False

    def give_me_apple(self):
        self.board.fill_board()
        self.board.set_board(self.wonsz.body)
        return self.board.get_zero_random_pos()
        