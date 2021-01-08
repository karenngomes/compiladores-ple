from semanthicanalyzer.states import StatesChain


class ReadChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.id_list = []

    def __begin(self, token):
        if token[0] == ')':
            self.state = self.__end

        if token[1] == 'id':
            # busca na tabela de simbolos e levanta erro se nao existir em nenhum escopos
            entry = self.scope_manager.search_identifier(token[0])
            self.id_list.append(entry)

    def __end(self, token):
        for entry in self.id_list:
            value = input("Aguardando Input: ")
            if value.isnumeric():
                entry.value = int(value)
            else:
                raise Exception(f'Read espera números inteiros')

        self._finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou
