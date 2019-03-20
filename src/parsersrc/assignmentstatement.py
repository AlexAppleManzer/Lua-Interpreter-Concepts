from pptree import Node

class AssignmentStatement:
    def __init__(self, var, expr, mem):
        self.var = var
        self.expr = expr
        self.mem = mem

    def execute(self):
        self.mem.store(self.var.get_char(), self.expr.evaluate())

    def gen_pptree(self, parent):
        Node("id", parent)
        Node("=", parent)
        self.expr.gen_pptree(Node("<expr>", parent))
