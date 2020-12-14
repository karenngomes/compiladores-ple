from SemanthicAnalyzer.states.StatesChain import StatesChain

class WriteChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super.__init__(self, args, kwargs)
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
            print(entry.value)
        
        self.__finalize() # ramo da maquina de estado chegou ao fim, precisa executar de onde parou