class JumpMaker(object):
    TOKEN_POS_INDEX = 2

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

        if token[0] in ['if', 'while', 'repeat', 'for']:
            self.push_stack(token.append(index))

        elif token[0] == 'end':
            pair = self.pop_stack()
            if pair[0] == 'if':
                next = self.tokens[index + 1] # token depois do end
                if next[0] == 'else':
                    pair.append(next[self.TOKEN_POS_INDEX]) # adiciona ao if atual o indice do else que faz par com ele
            else:
                token.append(pair[self.TOKEN_POS_INDEX]) # adiciona ao end atual o indice do inicio do seu loop

        elif token[0] == 'until':
            pair = self.pop_stack()
            token.append(pair[self.TOKEN_POS_INDEX]) # adiciona ao until atual o indice do inicio do seu loop
