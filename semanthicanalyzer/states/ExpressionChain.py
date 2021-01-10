from semanthicanalyzer.states import StatesChain


class ExpressionChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
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
            if entry.type == "integer": 
                value = entry.value
            #elif entry.category == "function":
            #    value = entry.value
            #    if value is None:
            #       raise Exception(f'Null Value')
            else:
                raise Exception(f'Expressao espera uma função ou variável inteira e recebeu {entry.category} do tipo {entry.type}')
        else:
            value = int(token[0])

        if self.accumulated_value is None:
            self.accumulated_value = value
        else:
            self.accumulated_value = self.solve_operation(self.accumulated_value, value)

    def __resolve_operator(self, token):
        if token[1] == "operador":
            self.state = self.__begin
            self.operator = token[0]
        else: # achou )
            self._finalize()  # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
            # impede que seja somado (+1) duas vezes no indice quando ExpressionChain é chamado por 
            # outra chain que não possui dois delimitadores finais, exemplo: quando AttributionChain
            # chama a ExpressionChain, a segunda termina em ; e a primeira termina no token inicial
            # de outro comando.
            self.index[0] -= 1
            return self.accumulated_value

    def solve_operation(self, op1, op2):
        if self.operator == '+':
            return op1 + op2
        elif self.operator == '-':
            return op1 - op2
        elif self.operator == '*':
            return op1 * op2
        elif self.operator == '/':
            if op2 == 0:
                raise(Exception("Divisão por 0!"))
            return op1 // op2 # divisao inteira

