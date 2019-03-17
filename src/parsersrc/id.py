
class Id:

    def __init__(self, char):

        if not char[0].isalpha():
            raise ValueError("invalid ID argument")
        self.char = char

    def get_char(self):
        return self.char

    def evaluate(self):
        # todo: make work
        return 0
