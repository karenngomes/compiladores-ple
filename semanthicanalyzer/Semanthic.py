from .states import ExpressionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class Semanthic(object):
    def __init__(self, tokens, scope_manager):
        self.index = [0]
        self.token_list = tokens
        self.scope_manager = scope_manager

    def analyze(self):
        # inicia a partir do begin do corpo, seu indice esta no token <programa>
        self.index[0] = self.token_list[0][TOKEN_POS_INDEX]
        while self.index[0] < len(self.token_list):
            token = self.token_list[self.index[0]]

            if token[0] == "read":
                chamar ReadChain(self.scope_manager, token)

            elif token[0] == "write":
                chamar WriteChain(self.scope_manager, token)

            elif token[0] == "for":
                chamar ForChain(self.scope_manager, token)

            elif token[0] == "repeat":

            elif token[1] == 'attributtion'
                chamar RepeatChain(self.scope_manager, token)

            elif token[0] == "while":
                chamar WhileChain(self.scope_manager, token)

            elif token[0] == "if":
                chamar IfChain(self.scope_manager, token)

            elif token[0] == 'else':
                self.index[0] = token[TOKEN_POS_INDEX]

            elif token[1] == "id" and self.token_list[self.index[0] + 1][1] == "attribution"
                chamar AttributionChain(self.scope_manager, token)

            else: # procedimento
                chamar ProcedureChain(self.scope_manager, token)

            self.index[0] += 1

