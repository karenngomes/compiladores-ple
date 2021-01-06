from semanthicanalyzer.states import StatesChain, BoolChain, RelationalChain


class ConditionChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.result = None
        
    def __begin(self, token):
        if (token[1] == 'boolean2'):
            Chain = BoolChain
        elif (token[1] == 'intnum'):
            Chain = RelationalChain
        else:
            entry = self.scope_manager.search_identifier(token[0])
            if entry.type == 'integer':
                Chain = RelationalChain
            else:
                Chain = BoolChain
        chain = Chain(self.scope_manager, self.token_list, self.index)
        self.result = chain.exec()
        self._finalize()
        return self.result
