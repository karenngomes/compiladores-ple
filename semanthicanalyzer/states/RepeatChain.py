from semanthicanalyzer.states import StatesChain, ConditionChain, WhileChain
from syntaticanalyzer import TOKEN_POS_INDEX

class RepeatChain(WhileChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = self._begin
    
    def _begin(self, token):
        super()._begin(token)
        self.state = self._resolve

    def _resolve(self, token):
        result = super()._resolve(token)
        if result:
            self.index[0] -= 1