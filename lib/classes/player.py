class Player:
    all =[]

    def __init__(self, username):
        self.username = username

        self.__class__.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_name):
        if type(new_name) == str and 1 < len(new_name) < 17:
            self._username = new_name
        else:
            raise Exception("Username must be a string between 2 and 16 characters.")

    def results(self):
        from classes.result import Result
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        # num_times = 0
        # for game_played in [result.game for result in self.results()]:
        #     if game_played == game:
        #         num_times = num_times + 1
        # return num_times

        return len([result for result in self.results() if result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        # highest_score = 0
        # highest_player = None
        # for player in cls.all:
        #     avg_score = game.average_score(player)
        #     if avg_score > highest_score:
        #         highest_score = avg_score
        #         highest_player = player
        # return highest_player
        return max(cls.all, key=lambda player : game.average_score(player))
    
    def __str__(self):
        return f"Player: {self.username}"
