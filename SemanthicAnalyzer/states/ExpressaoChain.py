from SemanthicAnalyzer.states.StatesChain import StatesChain

class ExpressaoChain(StatesChain):
    def __init__(self):
        super.__init__(self)
        self.accumulated_value = None
        self.operation = None
    
    def __init(self, token):
        # se valor_acumulado=None, entao valor_acumulado = token.value
        # senao, entao valor_acumulado = valor_acumulado op token.value
        # se state=; e operador=None, valor_acumulado=token.value
        # check scope
        if token[1] == 'id':
            #TODO: get_var
            value = self.scope_manager.get_var(token[0]) # busca na tabela de simbolos e levanta erro se nao existir em nenhum escopos
        elif token[1] == 'intnum':
            value = token[0]

        if self.accumulated_value is None:
            self.accumulated_value = value
        else:
            self.accumulated_value = self.solve_operation(self.accumulated_value, value)
            self.operation(value)
        
    def __resolve_operator(self, token):
        if token[1] == "operator": 
            self.operator = token[0]
        else:
            self.__finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
            return self.accumulated_value
            
    def solve_operation(self, op1, op2):
        if self.operator is '+':
            return op1 + op2
        elif self.operator is '-':
            return op1 - op2
        elif self.operator is '*':
            return op1 * op2
        elif self.operator is '/':
            return op1 // op2 # divisao inteira 
        