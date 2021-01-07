from semanthicanalyzer.states import StatesChain, ConditionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class IfChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.result = None
        self.else_token = None
        self.if_end_index = None

    def __begin(self, token):
        self.state = self.__resolve
        self.if_end_index = token[TOKEN_POS_INDEX] # index do end do if
        if self.token_list[self.if_end_index + 1][0] == 'else':
            self.else_token = self.token_list[self.if_end_index + 1]

    def __resolve(self, token):
        if token[0] == '(': return
        self.result = ConditionChain(self.scope_manager, self.token_list, self.index).exec()
        if self.result == True:
            self.index[0] += 2 # indice do then
        else:
            self.index[0] = self.if_end_index
            if self.else_token is not None:
                # Por padrão o else redireciona para seu end,
                # mas dessa forma ele redireciona para o token
                # seguinte
                self.else_token[TOKEN_POS_INDEX] = self.if_end_index + 2
        self._finalize()