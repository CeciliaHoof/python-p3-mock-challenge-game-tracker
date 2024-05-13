class Result:

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if type(value) == int and 0 < value < 5001 and not hasattr(self, 'score'):
            self._score = value
        else:
            raise Exception("Score must be between 1 and 5000")