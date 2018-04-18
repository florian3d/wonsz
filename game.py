from board import Board
from wonsz import Wonsz
from time import time
from speed import Speed
from high_score import HighScore

class Game():

    def __init__(self, rows=20, cols=20):

        self.board = Board(rows=rows, cols=cols)
        self.game_over = False
        self.score = 0
        self.high_score = HighScore()
        self.wonsz = Wonsz(self.board)
        self.apple = self.give_me_apple()
        self.speed = Speed()
        self.time = time()
        self.eat = False
        self.pause = True
        self.modes = ('Classic', 'Modern')
        self.mode = self.modes[0]
        self.steps = 0
        self.tiles = self.board.rows*self.board.cols
        self.points = self.tiles - self.steps
        self.debug = []

    def restart(self):

        self.board = Board()
        self.game_over = False
        self.score = 0
        self.wonsz = Wonsz(self.board)
        self.apple = self.give_me_apple()
        self.time = time()
        self.eat = False
        self.pause = True
        self.steps = 0
        self.points = self.tiles - self.steps

    def left(self):

        self.wonsz.direction = self.wonsz.directions.left
        
    def right(self):

        self.wonsz.direction = self.wonsz.directions.right
        
    def up(self):

        self.wonsz.direction = self.wonsz.directions.up
        
    def down(self):

        self.wonsz.direction = self.wonsz.directions.down

    def update(self):
        if not self.pause and not self.game_over:
            t0 = time()
            t = t0 - self.time
            if t > self.speed.value:
                self.time = time() # t0
                self._update_()
                return True
            return False

    def _update_(self):

        self.eat = False
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
            self.steps += 1
            self.points = self.tiles - self.steps + len(self.wonsz.body)
            if self.wonsz.body[0] == self.apple:
                self.score += self.points
                if self.score > self.high_score.value:
                    self.high_score.value = self.score
                self.eat = True
                self.apple = self.give_me_apple()
                self.steps = 0

            self.wonsz.body.insert(0, (row, col))
            if not self.eat:
                self.wonsz.body.pop()

    def give_me_apple(self):
        self.board.fill_board()
        self.board.set_board(self.wonsz.body)
        return self.board.get_zero_random_pos()
        