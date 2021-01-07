
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
            token.append(index)

        elif token[0] == 'end':
            #TODO: verificar se precisa adiconar uma condicional para o end do corpo do programa
            pair = self.pop_stack()
            if pair[0] == 'if' or pair[0] == 'else':
                pair[TOKEN_POS_INDEX] = index # adiciona dono do end atual o indice do end que faz par com ele
                token.append(index + 1)  # adiciona o indice do proximo token ao end
            else:
                token.append(pair[TOKEN_POS_INDEX]) # adiciona ao end atual o indice do seu dono
                pair[TOKEN_POS_INDEX] = index + 1  # adiciona ao token do loop o indice após seu end

        elif token[0] == 'until':
            pair = self.pop_stack()
            token.append(pair[TOKEN_POS_INDEX]) # adiciona ao until atual o indice do inicio do seu loop
            #pair = self.pop_stack()

