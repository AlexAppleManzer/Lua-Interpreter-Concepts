from pptree import Node

class BinaryExpression:
    # 0 = add op 1 = sub op 2 = mul op 3 = div op
    def __init__(self, op, expr1, expr2):
        if op is None:
            raise ValueError("null arithmetic op assignment")
        if expr1 is None or expr2 is None:
            raise ValueError("null arithmetic expr assignment")

        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        value = 0
        if self.op == 0:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == 1:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == 1:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == 1:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        return value

    def gen_pptree(self, parent):
        op = ('+', '-', '*', '/')
        self.expr1.gen_pptree(Node("<expr>", parent))
        Node(op[self.op], parent)
        self.expr1.gen_pptree(Node("<expr>", parent))
