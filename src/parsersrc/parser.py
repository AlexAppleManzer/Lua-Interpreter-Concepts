from parsersrc.tokens import Tokens
from parsersrc.lexcaller import LexCaller
from parsersrc import block as blk
from parsersrc import program as pgrm
from parsersrc.ifstatement import IfStatement

class Parser:

    def __init__(self):
        # constructor
        lex = LexCaller()
        self.tokenList = lex.get_all_data()
        self.tlp = 0
        # tlp = token list pointer

    def parse(self):
        # parses the lua code
        # check for function keyword
        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.function_keyword))
        self.tlp += 1
        # check for ( token
        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.left_paren))
        self.tlp += 1
        # check for ) token
        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.right_paren))
        self.tlp += 1
        # matches <block> statement
        block = self.get_block()
        # checks for end
        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.end_keyword))
        self.tlp += 1
        return pgrm.Program(block)

    def get_block(self):
        block = blk.Block()
        tok = self.tokenList[self.tlp]
        while(self.valid_start_stmt(tok)):
            stmt = self.get_stmt()
            block.add(stmt)
            tok = self.tokenList[self.tlp]
        return blk

    def valid_start_stmt(self, tok):
        return self.equals(tok, Tokens.id) or self.equals(tok, Tokens.if_keyword) \
               or self.equals(tok, Tokens.while_keyword) or self.equals(tok, Tokens.print_keyword) \
               or self.equals(tok, Tokens.repeat_keyword)

    def get_stmt(self):
        tok = self.tokenList[self.tlp]
        stmt = -1
        if self.equals(tok, Tokens.if_keyword):
            stmt = self.get_if_stmt()
        elif self.equals(tok, Tokens.while_keyword):
            stmt = self.get_while_stmt()
        elif self.equals(tok, Tokens.print_keyword):
            stmt = self.get_print_stmt()
        elif self.equals(tok, Tokens.repeat_keyword):
            stmt = self.get_repeat_stmt()
        elif self.equals(tok, Tokens.id):
            stmt = self.get_assign_stmt()
        else:
            print("uh oh, invalid statment")
        return stmt

    def get_if_stmt(self):
        stmt = "no"
        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.if_keyword))
        self.tlp += 1

        expr = self.get_bool_expr()

        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.then_keyword))
        self.tlp += 1

        blk1 = self.get_block()

        tok = self.tokenList[self.tlp]
        assert(self.equals(tok, Tokens.else_keyword))
        self.tlp += 1

        blk2 = self.get_block()

        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.end_keyword))
        self.tlp += 1

        return IfStatement(expr, blk1, blk2)

    def get_while_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    def get_print_stmt(self):
        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.print_keyword))
        self.tlp += 1

        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.end_keyword))
        self.tlp += 1

        expr = self.get_arithmetic_expr()

        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.end_keyword))
        self.tlp += 1

        return PrintStatement(expr)

    def get_repeat_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    def get_assign_stmt(self):
        var = self.get_id()
        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.assignment_operator))
        self.tlp += 1
        expr = self.get_arithmetic_expr()
        return AssignmentStatement(var, expr)

    def get_bool_expr(self):
        # eq = 0 ne = 1 gt = 2 ge = 3 lt = 4 le = 5
        tok = self.tokenList[self.tlp]
        if self.equals(tok, Tokens.eq_operator):
            op = 0
        elif self.equals(tok, Tokens.ne_operator):
            op = 1
        elif self.equals(tok, Tokens.gt_operator):
            op = 2
        elif self.equals(tok, Tokens.ge_operator):
            op = 3
        elif self.equals(tok, Tokens.lt_operator):
            op = 4
        elif self.equals(tok, Tokens.le_operator):
            op = 5
        self.tlp += 1
        expr1 = self.get_arithmetic_expr()
        expr2 = self.get_arithmetic_expr()
        return BooleanExpression(op, expr1, expr2)

    def get_arithmetic_expr(self):
        tok = self.tokenList[self.tlp]
        if self.equals(tok, Tokens.id):
            expr = self.get_id()
        elif self.equals(tok, Tokens.literal_integer):
            expr = self.get_literal_int()
        else:
            expr = self.get_bin_expr()
        return expr

    def get_id(self):
        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.id))
        self.tlp += 1
        return Id(tok[self.tlp-1][1])

    def get_literal_int(self):
        tok = self.tokenList[self.tlp]
        assert (self.equals(tok, Tokens.literal_integer))
        value = int(self.tokenList[self.tlp][1])
        return LiteralInteger(value)

    def get_bin_expr(self):

        # 0 = add op 1 = sub op 2 = mul op 3 = div op
        tok = self.tokenList[self.tlp]
        if self.equals(tok, Tokens.add_operator):
            op = 0
        elif self.equals(tok, Tokens.sub_operator):
            op = 1
        elif self.equals(tok, Tokens.mul_operator):
            op = 2
        elif self.equals(tok, Tokens.div_operator):
            op = 3
        self.tlp += 1
        expr1 = self.get_arithmetic_expr()
        expr2 = self.get_arithmetic_expr()
        return BinaryExpression(op, expr1, expr2)


    @staticmethod
    def equals(token, tokens):
        # checks to see if token = a tok type
        if token[0] == tokens.name():
            # self.token_index += 1
            return True
        else:
            return False
