from .states import ExpressaoChain

class Semanthic(object):
    def __init__(self, tokens, scope_manager):
        self.current_token_index = 0
        self.tokens = tokens
        self.scope_manager = scope_manager

    def analyze(self):
        index = 0
        while index < len(self.tokens):
            
            index += 1
    
    def __if(self, index):
        exp_chain = ExpressaoChain(self.scope_manager)
        while True:
            value = exp_chain.exec(tokens[index])
            if exp_chain.has_done(): break
            index += 1



