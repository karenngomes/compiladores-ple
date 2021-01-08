from semanthicanalyzer.states import StatesChain, ConditionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class IfChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.result = None
        self.else_token = None
        self.jump_index = None

    def __begin(self, token):
        self.state = self.__resolve
        self.jump_index = token[TOKEN_POS_INDEX] # para pegar o index do end do if
        big_jump = self.jump_index.big_jump_index
        if self.token_list[big_jump + 1][0] == 'else':
            self.else_token = self.token_list[big_jump + 1]

    def __resolve(self, token):
        if token[0] == '(': return
        self.result = ConditionChain(self.scope_manager, self.token_list, self.index).exec()
        if self.result == True:
            self.index[0] += 2 # indice do then
            self.else_token[TOKEN_POS_INDEX].jump_big = True # reseta o else para nao executar
        else:
            self.index[0] = self.jump_index.get_jump_index() #if's por padrão pulam grande
            if self.else_token is not None:
                # Por padrão o else redireciona para seu end,
                # mas dessa forma ele redireciona para o token
                # seguinte
                else_jump_index = self.else_token[TOKEN_POS_INDEX]
                else_jump_index.jump_big = False
                else_jump_index.small_jump = self.jump_index.big_jump_index + 2
        self._finalize()