from .StatesChain import StatesChain

class BoolChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.accumulated_value = None
        self.is_inverted = False # se um not inverteu a saida
        self.operator = None

    def __begin(self, token):
        # se valor_acumulado=None, entao valor_acumulado = token.value
        # senao, entao valor_acumulado = valor_acumulado op token.value
        # se state=; e operador=None, valor_acumulado=token.value
        # check scope
        if token[1] == 'id':
            self.state = self.__resolve_operator

            # busca na tabela de simbolos e levanta erro se nao existir em nenhum escopos
            entry = self.scope_manager.search_identifier(token[0])

            # verifica se eh uma variable do tipo booleano
            if entry.category == "variable" and entry.type == "boolean":
                value = entry.value
            else:
                raise Exception(f'Expressao espera uma variável booleana e recebeu {entry.category} do tipo {entry.type}');

            # inverte no caso de not
            if self.is_inverted == True:
                value = not value
                self.is_inverted = False

            # salva o valor acumulado
            if self.accumulated_value is None:
                self.accumulated_value = value
            else:
                self.accumulated_value = self.solve_operation(self.accumulated_value, value)

        else: # eh um boolean2(not)
            self.is_inverted = not self.is_inverted

    def __resolve_operator(self, token):
        if token[1] == "boolean1":
            self.state = self.__begin
            self.operator = token[0]
        else:
            self._finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
            # impede que seja somado (+1) duas vezes no indice quando ExpressionChain é chamado por 
            # outra chain
            return self.accumulated_value

    def solve_operation(self, op1, op2):
        if self.operator == 'and':
            return op1 and op2
        elif self.operator == 'or':
            return op1 or op2
