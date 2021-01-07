from semanthicanalyzer.states import StatesChain, ConditionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class WhileChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.post_end_index = None
    
    def __begin(self, token):
        self.state = self._resolve
        self.post_end_index = token[TOKEN_POS_INDEX]
    
    def _resolve(self, token):
        if token[0] == '(': return
            
        cond_chain = ConditionChain(self.scope_manager, self.token_list,
                                    self.index)
        is_true = cond_chain.exec()

        if is_true:
            self.index[0] += 2 # pula para o begin depois da condição
        else:
            self.index[0] = self.post_end_index # pula para o token depois do seu par "end"
            # essa alteração é feita no JumpMaker.
        self._finalize()
        return is_true
