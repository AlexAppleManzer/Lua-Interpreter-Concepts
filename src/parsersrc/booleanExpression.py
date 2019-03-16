from parsersrc.tokens import tokens

class BooleanExpression:
     def __init__(self):
         self.rationalOperator = [self.tokens.eq_operator, self.tokens.ge_operator, self.tokens.gt_operator, \
                                  self.tokens.ne_operator, self.tokens.lt_operator, self.tokens.le_operator]


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


