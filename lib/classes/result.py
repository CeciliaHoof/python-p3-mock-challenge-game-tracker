class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.__class__.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if type(new_score) == int and 0 < new_score < 5001 and not hasattr(self, 'score'):
            self._score = new_score
        else:
            raise Exception("Score must be an int and cannot be changed")
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("Player must be a Player")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        from classes.game import Game
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception("Game must be a Game")
    
    def __str__(self):
        return f'Game: {self.game}. Player: {self.player}. Score: {self.score}'