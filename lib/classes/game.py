class Game:
    all = []

    def __init__(self, title):
        self.title = title

        self.__class__.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str and not hasattr(self, 'title') and len(value) > 0:
            self._title = value
        else:
            raise Exception('Title must be a string and cannot be changed')
    
    def results(self):
        from classes.result import Result
        return [result for result in Result.all if result.game == self]
    
    def players(self):
        return list(set(result.player for result in self.results()))
    
    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return 0