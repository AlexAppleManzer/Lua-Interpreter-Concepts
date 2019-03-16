from parsersrc.tokens import Tokens

class BooleanExpression:
     def __init__(self):
         self.rationalOperator = [Tokens.eq_operator, Tokens.ge_operator, Tokens.gt_operator,
                                  Tokens.ne_operator, Tokens.lt_operator, Tokens.le_operator]


     def booleanExpression(self, operator, expr1, expr2):
            self.operator = operator
            self.expr1 = expr1
            self.expr2 = expr2
          if (operator == None)
              print("error operator argument ")
          if expr1 == None or expr2 == None
              print("error arithmetic expression")



     def evaluate(self):
        self.result = False


