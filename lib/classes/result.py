from classes.player import Player
from classes.game import Game

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
    
        Result.all.append(self)
        
        self.player._results.append(self)
        self.player._games_played.append(self.game)

        self.game._results.append(self)
        self.game._players.append(self.player)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if type(value) == int and 0 < value < 5001 and not hasattr(self, 'score'):
            self._score = value
        else:
            raise Exception("Score must be between 1 and 5000")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if isinstance(value, Player):
            self._player = value
        else:
            raise Exception("Player must be of type Player")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if isinstance(value, Game):
            self._game = value
        else:
            raise Exception("Game must be of type Game")