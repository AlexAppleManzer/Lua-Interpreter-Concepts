from parsersrc.tokens import Tokens
from parsersrc.lexcaller import LexCaller
from parsersrc.block import Block
from parsersrc.id import Id
from parsersrc.whilestatement import WhileStatement
from parsersrc.printstatement import PrintStatement
from parsersrc.repeatstatment import RepeatStatement
from parsersrc.assignmentstatement import AssignmentStatement
from parsersrc.booleanexpression import BooleanExpression
from parsersrc.literalint import LiteralInteger
from parsersrc.binaryexpression import BinaryExpression
from parsersrc.memory import Memory
from parsersrc import program as pgrm
from parsersrc.ifstatement import IfStatement


class Parser:

    def __init__(self, file):
        # constructor
        lex = LexCaller()
        lex.change_file(file)
        self.tokenList = lex.get_all_data()
        lex.close_server()
        self.tlp = 0
        self.mem = Memory()
        # tlp = token list pointer

    def parse(self):
        # parses the lua code
        # check for function keyword
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.function_keyword, 1)
        self.tlp += 1

        id = self.get_id()
        # check for ( token
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.left_paren, 1)
        self.tlp += 1
        # check for ) token
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.right_paren, 1)
        self.tlp += 1
        # matches <block> statement
        block = self.get_block()
        # checks for end
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.end_keyword, 1)
        self.tlp += 1
        return pgrm.Program(block, id)

    def get_block(self):
        block = Block()
        tok = self.tokenList[self.tlp]
        while self.valid_start_stmt(tok):
            stmt = self.get_stmt()
            block.add(stmt)
            tok = self.tokenList[self.tlp]
        return block

    def valid_start_stmt(self, tok):
        return self.equals(tok, Tokens.id, 0) or self.equals(tok, Tokens.if_keyword, 0) \
               or self.equals(tok, Tokens.while_keyword, 0) or self.equals(tok, Tokens.print_keyword, 0) \
               or self.equals(tok, Tokens.repeat_keyword, 0)

    def get_stmt(self):
        tok = self.tokenList[self.tlp]
        stmt = -1
        if self.equals(tok, Tokens.if_keyword, 0):
            stmt = self.get_if_stmt()
        elif self.equals(tok, Tokens.while_keyword, 0):
            stmt = self.get_while_stmt()
        elif self.equals(tok, Tokens.print_keyword, 0):
            stmt = self.get_print_stmt()
        elif self.equals(tok, Tokens.repeat_keyword, 0):
            stmt = self.get_repeat_stmt()
        elif self.equals(tok, Tokens.id, 0):
            stmt = self.get_assign_stmt()
        else:
            print("uh oh, invalid statment")
        return stmt

    def get_if_stmt(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.if_keyword, 1)
        self.tlp += 1

        expr = self.get_bool_expr()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.then_keyword, 1)
        self.tlp += 1

        blk1 = self.get_block()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.else_keyword, 1)
        self.tlp += 1

        blk2 = self.get_block()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.end_keyword, 1)
        self.tlp += 1

        return IfStatement(expr, blk1, blk2)

    def get_while_stmt(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.while_keyword, 1)
        self.tlp += 1

        expr = self.get_bool_expr()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.do_keyword, 1)
        self.tlp += 1

        blk = self.get_block()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.end_keyword, 1)
        self.tlp += 1

        return WhileStatement(expr, blk)

    def get_print_stmt(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.print_keyword, 1)
        self.tlp += 1

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.left_paren, 1)
        self.tlp += 1

        expr = self.get_arithmetic_expr()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.right_paren, 1)
        self.tlp += 1

        return PrintStatement(expr)

    def get_repeat_stmt(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.repeat_keyword, 1)
        self.tlp += 1

        blk = self.get_block()

        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.until_keyword, 1)
        self.tlp += 1

        expr = self.get_bool_expr()

        return RepeatStatement(blk, expr)

    def get_assign_stmt(self):
        var = self.get_id()
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.assignment_operator, 1)
        self.tlp += 1
        expr = self.get_arithmetic_expr()
        return AssignmentStatement(var, expr, self.mem)

    def get_bool_expr(self):
        # eq = 0 ne = 1 gt = 2 ge = 3 lt = 4 le = 5
        tok = self.tokenList[self.tlp]
        op = -1
        if self.equals(tok, Tokens.eq_operator, 0):
            op = 0
        elif self.equals(tok, Tokens.ne_operator, 0):
            op = 1
        elif self.equals(tok, Tokens.gt_operator, 0):
            op = 2
        elif self.equals(tok, Tokens.ge_operator, 0):
            op = 3
        elif self.equals(tok, Tokens.lt_operator, 0):
            op = 4
        elif self.equals(tok, Tokens.le_operator, 0):
            op = 5
        self.tlp += 1
        expr1 = self.get_arithmetic_expr()
        expr2 = self.get_arithmetic_expr()
        return BooleanExpression(op, expr1, expr2)

    def get_arithmetic_expr(self):
        tok = self.tokenList[self.tlp]
        if self.equals(tok, Tokens.id, 0):
            expr = self.get_id()
        elif self.equals(tok, Tokens.literal_integer, 0):
            expr = self.get_literal_int()
        else:
            expr = self.get_bin_expr()
        return expr

    def get_id(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.id, 1)
        self.tlp += 1
        return Id(tok[1], self.mem)

    def get_literal_int(self):
        tok = self.tokenList[self.tlp]
        self.equals(tok, Tokens.literal_integer, 1)
        value = int(self.tokenList[self.tlp][1])
        self.tlp += 1
        return LiteralInteger(value)

    def get_bin_expr(self):

        # 0 = add op 1 = sub op 2 = mul op 3 = div op
        tok = self.tokenList[self.tlp]
        op = -1
        if self.equals(tok, Tokens.add_operator, 0):
            op = 0
        elif self.equals(tok, Tokens.sub_operator, 0):
            op = 1
        elif self.equals(tok, Tokens.mul_operator, 0):
            op = 2
        elif self.equals(tok, Tokens.div_operator, 0):
            op = 3
        self.tlp += 1
        expr1 = self.get_arithmetic_expr()
        expr2 = self.get_arithmetic_expr()
        return BinaryExpression(op, expr1, expr2)


    @staticmethod
    def equals(token, tokens, error):
        # checks to see if token = a tok type
        if token[0] == tokens.name:
            # self.token_index += 1
            return True
        else:
            if error:
                raise ValueError("Found {} but expected {} around line {}".format(token[1], tokens.name, int(token[2]) +1))
            return False
