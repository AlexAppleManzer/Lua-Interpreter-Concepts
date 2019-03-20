from pptree import Node


class WhileStatement:
    def __init__(self, expr, blk):
        if expr is None:
            raise ValueError("null bool expression arg")
        if blk is None:
            raise ValueError("null block argument")
        self.expr = expr
        self.blk = blk

    def execute(self):
        while self.expr.evaluate():
            self.blk.execute()

    def gen_pptree(self, parent):
        Node("repeat", parent)
        self.expr.gen_pptree(Node("<bool_expr>", parent))
        Node("do", parent)
        self.blk.gen_pptree(Node("<block>", parent))
