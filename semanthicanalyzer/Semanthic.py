from .states import ExpressionChain
from syntaticanalyzer import JumpMaker

class Semanthic(object):
    def __init__(self, tokens, scope_manager):
        self.index = [0]
        self.token_list = tokens
        self.scope_manager = scope_manager

    def analyze(self):
        # inicia a partir do begin do corpo, seu indice esta no token <programa>
        index = self.token_list[0][JumpMaker.TOKEN_POS_INDEX]
        while index < len(self.token_list):
            token = self.token_list[index]
            
            if token[0] == "read":
                chamar ReadChain(self.scope_manager, token)
            
            elif token[0] == "write":
                chamar WriteChain(self.scope_manager, token)

            elif token[0] == "for":
                chamar ForChain(self.scope_manager, token)

            elif token[0] == "repeat":
    
        if token[1] == 'attribut'

                chamar RepeatChain(self.scope_manager, token)
            
            elif token[0] == "while":
                    chamar WhileChain(self.scope_manager, token)

            elif token[0] == "if":
                chamar IfChain(self.scope_manager, token)
            
            elif token[1] == "id" and self.token_list[index + 1][1] == "attribution"
                chamar AttributionChain(self.scope_manager, token)
            
            else: # procedimento
                chamar ProcedureChain(self.scope_manager, token)

            index += 1

    def expression(self, index):
        exp_chain = ExpressionChain(self.scope_manager)
        while True:
            value = exp_chain.run(tokens[index])
            if exp_chain.has_done(): break
            index += 1