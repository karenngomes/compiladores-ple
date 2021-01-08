from semanthicanalyzer.states import StatesChain, ConditionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class RepeatChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.jump_index = None
    
    def __begin(self, token):
        self.state = self.__resolve
        self.jump_index = token[TOKEN_POS_INDEX]
    
    def __resolve(self, token):
        if token[0] == '(': return
            
        cond_chain = ConditionChain(self.scope_manager, self.token_list,
                                    self.index)
        is_true = cond_chain.exec()

        if is_true:
            self.jump_index.jump_big = False
            self.index[0] += 1 # pula para o begin depois da condição
        else:
            self.jump_index.jump_big = True
            self.index[0] = self.jump_index.big_jump_index # pula para o token depois do seu par "end"
            # essa alteração é feita no JumpMaker.
        self._finalize()