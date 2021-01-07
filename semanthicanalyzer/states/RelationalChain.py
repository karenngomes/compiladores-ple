from semanthicanalyzer.states import StatesChain, ExpressionChain

class RelationalChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.first_operand = None
        self.result = None
        self.operator = None

    def __begin(self, token):
        self.state = self.__resolve_relational
        exp_chain = ExpressionChain(self.scope_manager, self.token_list, self.index)
        value = exp_chain.exec()
    
        if self.first_operand is None:
            self.first_operand = value
        else:
            self.result = self.solve_operation(self.first_operand, value)

    def __resolve_relational(self, token):
        if token[1] == 'relacao':
            self.state = self.__begin
            self.operator = token[0]
        else:
            self._finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
            return self.result

    def solve_operation(self, op1, op2):
        if self.operator == '>':
            return op1 > op2
        elif self.operator == '<':
            return op1 < op2
        elif self.operator == '=':
            return op1 == op2
        elif self.operator == '<>':
            return op1 != op2
        elif self.operator == '<=':
            return op1 <= op2
        elif self.operator == '>=':
            return op1 >= op2

