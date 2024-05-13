class Player:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if type(value) == str and 1 < len(value) < 17:
            self._username = value
        else:
            raise Exception("Username must be a string between 2 nd 16 characters")