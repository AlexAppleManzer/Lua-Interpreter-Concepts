from parsersrc.tokens import Tokens
from parsersrc.lexcaller import LexCaller
from parsersrc import block as blk
from parsersrc import program as pgrm

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
        print("D:")
        stmt = "no"
        return stmt

    def get_while_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    def get_print_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    def get_repeat_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    def get_assign_stmt(self):
        print("D:")
        stmt = "no"
        return stmt

    @staticmethod
    def equals(token, tokens):
        # checks to see if token = a tok type
        if token[0] == tokens.name():
            # self.token_index += 1
            return True
        else:
            return False
