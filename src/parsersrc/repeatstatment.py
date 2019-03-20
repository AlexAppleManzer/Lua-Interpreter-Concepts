from pptree import Node


class RepeatStatement:
    def __init__(self, blk, expr):
        if blk is None:
            raise ValueError("null block arguement")
        if expr is None:
            raise ValueError("null bool expr arguement")
        self.blk = blk
        self.expr = expr

    def execute(self):
        while True:
            self.blk.execute()
            if self.expr.evaluate():
                break

    def gen_pptree(self, parent):
        Node("repeat", parent)
        self.blk.gen_pptree(Node("<block>", parent))
        Node("until", parent)
        self.expr.gen_pptree(Node("<bool_expr>", parent))
