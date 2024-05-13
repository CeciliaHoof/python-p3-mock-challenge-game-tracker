class Player:
    all = []

    def __init__(self, username):
        self.username = username

        self.__class__.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if type(value) == str and 1 < len(value) < 17:
            self._username = value
        else:
            raise Exception("Username must be a string between 2 nd 16 characters")

    def results(self):
        from classes.result import Result
        return [result for result in Result.all if result.player == self]
    
    def games_played(self):
        return list(set(result.game for result in self.results()))
    
    def played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])