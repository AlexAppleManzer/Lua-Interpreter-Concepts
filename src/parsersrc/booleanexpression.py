from parsersrc.tokens import Tokens
from pptree import Node


class BooleanExpression:

    def __init__(self, operator, expr1, expr2):
        self.rationalOperator = (Tokens.eq_operator, Tokens.ge_operator, Tokens.gt_operator,
                                 Tokens.ne_operator, Tokens.lt_operator, Tokens.le_operator)
        self.operator = operator
        self.expr1 = expr1
        self.expr2 = expr2
        if operator is None:
            print("error operator argument ")
        if expr1 is None or expr2 is None:
            print("error arithmetic expression")

    def evaluate(self):
        # eq = 0 ne = 1 gt = 2 ge = 3 lt = 4 le = 5
        result = False
        if self.operator == 0:
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.operator == 1:
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif self.operator == 2:
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.operator == 3:
            result = self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.operator == 4:
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.operator == 5:
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        return result

    def gen_pptree(self, parent):
        op = ('==', '!=', '>', '>=', '<', '<=')
        self.expr1.gen_pptree(Node("<expr>", parent))
        Node(op[self.operator], parent)
        self.expr2.gen_pptree(Node("<expr>", parent))
