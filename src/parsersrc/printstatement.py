class PrintStatement:
    def __init__(self, expr):
        self.expr = expr

    def execute(self):
        print(self.expr.evaluate)
