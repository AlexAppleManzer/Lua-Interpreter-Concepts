from parsersrc import block as blk

class IfStatement():
    def __init__(self):
        self.blk = blk

    def ifstatement(self, expr, blk, blk2 ):
        self.expr = expr
        self.blk = blk
        self.blk2 = blk2

    def execute(self):

