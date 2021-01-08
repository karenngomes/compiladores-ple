from syntaticanalyzer import JumpIndex


TOKEN_POS_INDEX = 2

class JumpMaker(object):

    def __init__(self, tokens):
        self.begin_stack = []
        self.end_stack = []
        self.tokens = tokens

    def push_end_stack(self, token):
        self.end_stack.append(token)

    def pop_end_stack(self):
        return self.end_stack.pop()
    
    def push_begin_stack(self, token):
        self.begin_stack.append(token)

    def pop_begin_stack(self):
        return self.begin_stack.pop()

    def analyze(self, token, index):
        jump_points = ['if', 'else', 'while', 'repeat', 'for', 'program', 'procedure', 'function']
        if token[0] in jump_points:
            token.append(JumpIndex(small_jump=index))
            self.push_begin_stack(token)
            self.push_end_stack(token)

        elif token[0] == 'begin':
            self.__handle_begin(token, index)

        elif token[0] == 'end':
            self.__handle_end(token, index)

        elif token[0] == 'until':
            self.pop_begin_stack()
            pair = self.pop_end_stack()
            token.append(pair[TOKEN_POS_INDEX]) # adiciona ao until atual o indice do inicio do seu loop
            #pair = self.pop_end_stack()

    def __handle_end(self, token, index):
        #TODO: verificar se precisa adiconar uma condicional para o end do corpo do programa
        pair = self.pop_end_stack()
        if pair[0] == 'if' or pair[0] == 'else':
            pair_jump = pair[TOKEN_POS_INDEX] # recupera o indice do end que faz par com o token atual
            pair_jump.jump_big = True # coloca como padrao pular para o end
            pair_jump.big_jump_index = index # adiciona esse indice ao token atual
            token.append(JumpIndex(small_jump=index+1))  # adiciona o indice do proximo token ao end
        elif pair[0] == 'program':
            token.append(JumpIndex(small_jump=index+1)) # faz com que o end do program siga em frente
        else:
            pair_small_jump = pair[TOKEN_POS_INDEX].small_jump_index
            token.append(JumpIndex(small_jump=index+1,
                                   big_jump=pair_small_jump, 
                                   jump_big=True)) # adiciona ao end atual o indice do seu dono

            pair[TOKEN_POS_INDEX].big_jump_index = index + 1  # adiciona ao token do loop o indice após seu end
    
    
    def __handle_begin(self, token, index):
        pair = self.pop_begin_stack()
        if pair[0] == 'program':
            jump = pair[TOKEN_POS_INDEX]
            jump.jump_big = True
            jump.big_jump_index = index