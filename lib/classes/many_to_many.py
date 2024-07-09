class Game:
    def __init__(self,title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, val):
        if type(val) == str and not hasattr(self, 'title') and len(val) > 0:
            self._title = val
    
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in Result.all if result.game == self))
    
    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return 0


class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, val):
        if type(val) == str and 2 <= len(val) <= 16:
            self._username = val

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in Result.all if result.player == self))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:
    all =[]

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.__class__.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, val):
        if type(val) == int and 0 < val < 5001 and not hasattr(self, 'score'):
            self._score = val
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, val):
        if isinstance(val, Player):
            self._player = val
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, val):
        if isinstance(val, Game):
            self._game = val
    