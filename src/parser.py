from parsersrc import parser
FILE = input("File number?")

p = parser.Parser("test{}.lua".format(FILE))
program = p.parse()
program.execute()

