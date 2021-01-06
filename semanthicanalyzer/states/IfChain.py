from semanthicanalyzer.states import StatesChain, ConditionChain
from syntaticanalyzer import TOKEN_POS_INDEX

class IfChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.result = None
        self.end_index = None

    def __begin(self, token):
        self.end_index = token[TOKEN_POS_INDEX] # index do end do if
        self.result = ConditionChain(self.scope_manager, self.token_list, self.index).exec()

        if self.result == True:
            self.index[0] += 1
        else:
            self.index[0] = self.end_index

        self._finalize()
