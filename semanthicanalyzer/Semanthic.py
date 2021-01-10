from semanthicanalyzer import states
from syntaticanalyzer import TOKEN_POS_INDEX

class Semanthic(object):
    def __init__(self, tokens, scope_manager, begin=0, end=-1):
        self.index = [0]
        self.token_list = tokens
        self.begin = begin
        self.end = len(tokens) if end == -1 else end
        self.scope_manager = scope_manager

    def analyze(self):
        # inicia a partir do begin do corpo, seu indice esta no token <programa>
        if self.begin == 0:
            self.index[0] = self.token_list[0][TOKEN_POS_INDEX].get_jump_index()
        else: 
            self.index[0] = self.begin
        while self.index[0] < self.end:
            token = self.token_list[self.index[0]]

            if token[0] == "read":
                states.ReadChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "write":
                states.WriteChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "for" or token[0] == "to":
                states.ForChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "until":
                states.RepeatChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "while":
                states.WhileChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == "if":
                states.IfChain(self.scope_manager, self.token_list, self.index).exec()

            elif token[0] == 'else' or token[0] == 'end': # checar JumpMaker
                self.index[0] = token[TOKEN_POS_INDEX].get_jump_index()
                self.index[0] -= 1 # para nao andar dois tokens de uma vez

            elif token[1] == "id":
                entry = self.scope_manager.search_identifier(token[0])
                if self.token_list[self.index[0] + 1][1] == "attribution":
                    states.AttributionChain(self.scope_manager, self.token_list, self.index).exec()
                elif entry.category == 'function' or entry.category == 'procedure':
                    states.RoutineChain(self.scope_manager, self.token_list, self.index).exec()
                    pass
                
            else: # tokens sem função semântica
                pass

            self.index[0] += 1

