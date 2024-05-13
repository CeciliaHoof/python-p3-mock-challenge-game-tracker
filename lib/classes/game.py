class Game:

    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if type(value) == str and not hasattr(self, 'title'):
            self._title = value
        else:
            raise Exception('Title must be a string and cannot be changed')