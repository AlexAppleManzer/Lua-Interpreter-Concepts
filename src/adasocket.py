from parsersrc import parser
from pptree import *
import socket
import sys
sys.stdout = open('out.txt', 'w')
print('test')
FILE = 5


def run_parser():
    p = parser.Parser("test{}.lua".format(FILE))
    program = p.parse()
    program.execute()
    tree = program.gen_pptree()
    print_tree(tree)


s = socket.socket()
print("socket initilized")

port = 8889

s.bind(('', port))

s.listen(5)
print("its listening")

while True:
    c, addr = s.accept()

    c.send()