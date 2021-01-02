from semanthicanalyzer.states.StatesChain import StatesChain

__all__ = ['ExpressionChain']

class ExpressionChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = self.__begin
        self.accumulated_value = None
        self.operator = None

    def __begin(self, token):
        # se valor_acumulado=None, entao valor_acumulado = token.value
        # senao, entao valor_acumulado = valor_acumulado op token.value
        # se state=; e operador=None, valor_acumulado=token.value
        # check scope
        self.state = self.__resolve_operator
        if token[1] == 'id':
            # busca na tabela de simbolos e levanta erro se nao existir em nenhum escopos
            entry = self.scope_manager.search_identifier(token[0])
            # verifica se eh uma variable do tipo inteiro
            if entry.category == "variable" and entry.type == "integer": 
                value = entry.value
            else:
                raise Exception(f'Expressao espera uma variável inteira e recebeu {entry.category} do tipo {entry.type}')
        else:
            value = int(token[0])

        if self.accumulated_value is None:
            self.accumulated_value = value
        else:
            self.accumulated_value = self.solve_operation(self.accumulated_value, value)

    def __resolve_operator(self, token):
        if token[1] == "operator":
            self.state = self.__begin
            self.operator = token[0]
        else:
            self._finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
            return self.accumulated_value

    def solve_operation(self, op1, op2):
        if self.operator == '+':
            return op1 + op2
        elif self.operator == '-':
            return op1 - op2
        elif self.operator == '*':
            return op1 * op2
        elif self.operator == '/':
            return op1 // op2 # divisao inteira

