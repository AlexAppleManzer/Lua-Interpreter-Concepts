from pptree import Node

class IfStatement:
    def __init__(self, expr, blk, blk2 ):

        if expr is None:
            raise ValueError("no bool expr argument")
        if blk is None or blk2 is None:
            raise ValueError("no block argument")
        self.expr = expr
        self.blk = blk
        self.blk2 = blk2

    def execute(self):
        if self.expr.evaluate():
            self.blk.execute()
        else:
            self.blk2.execute()

    def gen_pptree(self, parent):
        Node("if", parent)
        self.expr.gen_pptree(Node("<bool_expr>", parent))
        Node("then", parent)
        self.blk.gen_pptree(Node("<expr>", parent))
        Node("else", parent)
        self.blk2.gen_pptree(Node("<expr>", parent))
