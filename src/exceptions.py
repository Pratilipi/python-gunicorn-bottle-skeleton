# db
class DbConnectionError(Exception):
    def __init__(self, err):
        self.message = 'db connection issue; {}'.format(err)
    def __str__(self):
        return str(self.message)

class DbInsertError(Exception):
    def __init__(self, err):
        self.message = 'db insertion issue; {}'.format(err)
    def __str__(self):
        return str(self.message)

class DbSelectError(Exception):
    def __init__(self, err):
        self.message = 'db select issue; {}'.format(err)
    def __str__(self):
        return str(self.message)

class DbUpdateError(Exception):
    def __init__(self, err):
        self.message = 'db update issue; {}'.format(err)
    def __str__(self):
        return str(self.message)

