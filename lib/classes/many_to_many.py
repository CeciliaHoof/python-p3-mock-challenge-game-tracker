class Game:
    def __init__(self, title):
        self.title = title

        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if type(new_title) == str and len(new_title) > 0 and not hasattr(self, "title"):
            self._title = new_title
        else:
            raise Exception("Title must be a string and cannot be changed")

    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        return sum(player_scores) / len(player_scores)
        
    def __str__(self):
        return f"Game: {self.title}"

class Player:
    all =[]

    def __init__(self, username):
        self.username = username

        self._results = []
        self._games_played = []

        Player.all.append(self)

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
        return self._results

    def games_played(self):
        return list(set(self._games_played))

    def played_game(self, game):
        return game in self._games_played

    def num_times_played(self, game):
        num_times = 0
        for game_played in self._games_played:
            if game_played == game:
                num_times = num_times + 1
        return num_times
    
    @classmethod
    def highest_scored(cls, game):
        highest_score = 0
        highest_player = None
        for player in cls.all:
            games_played = player.games_played()
            if game in games_played:  
                avg_score = game.average_score(player)
                if avg_score > highest_score:
                    highest_score = avg_score
                    highest_player = player
        return highest_player
    
    def __str__(self):
        return f"Player: {self.username}"

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.player._results.append(self)
        self.player._games_played.append(self.game)

        self.game._results.append(self)
        self.game._players.append(self.player)

        Result.all.append(self)

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
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("Player must be a Player")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception("Game must be a Game")
    
    def __str__(self):
        return f'Game: {self.game}. Player: {self.player}. Score: {self.score}'

game_1 = Game("Skribbl.io")
game_2 = Game("Scattegories")
player_1 = Player("Saaammmm")
player_2 = Player("ActuallyTopher")
Result(player_1, game_1, 2000)
Result(player_1, game_2, 19)
Result(player_1, game_1, 1900)
Result(player_2, game_2, 9)

for game in player_1.games_played():
    print(game)
print(player_1.num_times_played(game_1))