from parsersrc import parser
from pptree import *

FILE = 1

p = parser.Parser("test{}.lua".format(FILE))
program = p.parse()
program.execute()
tree = program.gen_pptree()
print_tree(tree)
