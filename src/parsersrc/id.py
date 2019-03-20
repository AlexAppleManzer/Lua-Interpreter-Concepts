from pptree import Node
class Id:

    def __init__(self, char, memory):
        self.memory = memory
        if not char[0].isalpha():
            raise ValueError("invalid ID argument")
        self.char = char[0]

    def get_char(self):
        return self.char

    def evaluate(self):
        # retrieves from memory
        return self.memory.get(self.char)

    def gen_pptree(self, parent):
        Node("id", parent)
