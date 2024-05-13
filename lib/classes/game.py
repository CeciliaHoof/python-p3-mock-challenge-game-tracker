class Game:

    def __init__(self, title):
        self.title = title

        self._results = []
        self._players = []
    
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
        return self._results
    
    def players(self):
        return list(set(self._players))