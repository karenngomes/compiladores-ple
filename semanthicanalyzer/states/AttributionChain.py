#from semanthicanalyzer.states import StatesChain
#from semanthicanalyzer.states import ExpressionChain
from semanthicanalyzer import states

class AttributionChain(states.StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.entry = None

    def __begin(self, token):
        self.entry = self.scope_manager.search_identifier(token[0])

        self.state = self.__attribution
    
    def __attribution(self, token):
        if token[0] == ':=': 
            return
        else:
            self.__call_expression_chain()

    def __call_expression_chain(self):
        exp_chain = states.ExpressionChain(self.scope_manager, 
                                   self.token_list,
                                   self.index)
        self.entry.value = exp_chain.exec()
        if self.entry.type == 'boolean' and self.entry.value != 0:
            self.entry.value = 1
        self._finalize()
            