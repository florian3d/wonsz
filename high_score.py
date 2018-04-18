class HighScore:

    def __init__(self):

        self._file_name_ = 'high_score.txt'
        self.value = 0
        self.get_high_score()

    def get_high_score(self):

        try:
            with open(self._file_name_, 'r') as f:
                value = f.read()
                if value:
                    self.value = int(value)
        except IOError as err:
            print(err)
        
    def save_high_score(self):

        try:
            with open(self._file_name_, 'w') as f:
                f.write(str(self.value))
        except IOError as err:
            print(err)
