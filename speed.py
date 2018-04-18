class Speed:

    def __init__(self):

        self.EASY = 'EASY'
        self.MEDIUM = 'MEDIUM'
        self.HARD = 'HARD'
        self.speeds = {self.EASY:0.2, self.MEDIUM:0.1, self.HARD:0.075}
        self.name = self.EASY
        self.value = self.speeds[self.name]

    def change_speed(self, name):

        
        if name in self.speeds:
            self.name = name
            self.value = self.speeds[self.name]
