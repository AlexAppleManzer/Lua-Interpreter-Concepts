from pptree import Node


class LiteralInteger:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def gen_pptree(self, parent):
        Node("lit_int", parent)
