from semanthicanalyzer import states
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
                states.ReadChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "write":
                states.WriteChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "for":
                #ForChain(self.scope_manager, self.token_list, self.index).exec()
                pass

            elif token[0] == "until":
                states.RepeatChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "while":
                states.WhileChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "if":
                states.IfChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == 'else' or token[0] == 'end': # checar JumpMaker
                self.index[0] = token[TOKEN_POS_INDEX].get_jump_index()
                self.index[0] -= 1 # para nao andar dois tokens de uma vez

            elif token[1] == "id" and self.token_list[self.index[0] + 1][1] == "attribution":
                states.AttributionChain(self.scope_manager, self.token_list, self.index).exec()

            else: # procedimento
                #states.ProcedureChain(self.scope_manager, self.token_list, self.index).exec()
                pass

            self.index[0] += 1

