from pptree import *


class Program:
    def __init__(self, blk, id):
        if blk is None:
            raise ValueError("null block arg")
        self.blk = blk
        self.id = id

    def __str__(self):
        return "<program> -> function id ( ) <block> end\n" + str(self.blk)


    def execute(self):
        self.blk.execute()

    def gen_pptree(self):
        root = Node("<program>")
        Node("funcion", root)
        Node("id", root)
        self.blk.gen_pptree(Node("<block>", root))
        Node("end", root)
        return root
