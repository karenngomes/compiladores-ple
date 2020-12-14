from .states import ExpressionChain

class Semanthic(object):
    def __init__(self, tokens, scope_manager):
        self.current_token_index = 0
        self.tokens = tokens
        self.scope_manager = scope_manager

    def analyze(self):
        index = 0
        while index < len(self.tokens):

            index += 1

    def expression(self, index):
        exp_chain = ExpressionChain(self.scope_manager)
        while True:
            value = exp_chain.run(tokens[index])
            if exp_chain.has_done(): break
            index += 1



