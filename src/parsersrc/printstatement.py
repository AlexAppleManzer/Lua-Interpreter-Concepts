from pptree import Node


class PrintStatement:
    def __init__(self, expr):
        if expr is None:
            raise ValueError("null arithmetic expression")
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate())

    def gen_pptree(self, parent):
        Node("print", parent)
        Node("(", parent)
        self.expr.gen_pptree(Node("<expr>", parent))
        Node(")", parent)
