from pptree import Node

class Block:
    def __init__(self):
        self.stmts = []

    def add(self, statment):
        if self.stmts is None:
            print("empty statement arguement")
        self.stmts.append(statment)

    def execute(self):
        for stmt in self.stmts:
            stmt.execute()

    def gen_pptree(self, parent):
        for stmt in self.stmts:
            stmt.gen_pptree(Node("<stmt>", parent))
