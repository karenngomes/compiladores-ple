
TOKEN_POS_INDEX = 2

class JumpMaker(object):

    def __init__(self, tokens):
        self.stack = []
        self.tokens = tokens

    def push_stack(self, token):
        self.stack.append(token)

    def pop_stack(self, token):
        self.stack.pop()

    def analyze(self, token, index):
        if len(self.stack) == 0: # se pilha esta vazia o programa acabou
            return

        if token[0] in ['if', 'else', 'while', 'repeat', 'for']:
            self.push_stack(token.append(index))

        elif token[0] == 'end':
            pair = self.pop_stack()
            if pair[0] == 'if' or pair[0] == 'else':
                pair[TOKEN_POS_INDEX] = index # adiciona ao if ou else atual o indice do end que faz par com ele
            else:
                token.append(pair[TOKEN_POS_INDEX]) # adiciona ao end atual o indice do inicio do seu loop

        elif token[0] == 'until':
            pair = self.pop_stack()
            token.append(pair[TOKEN_POS_INDEX]) # adiciona ao until atual o indice do inicio do seu loop
            pair = self.pop_stack()

