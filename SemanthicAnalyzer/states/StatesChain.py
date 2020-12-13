class StatesChain(object):
    def __init__(self, scope_manager):
        self.state = self.__init
        self.scope_manager = scope_manager
        self.__done = False # determina se o ramo da maquina de estado chegou num estado final
    
    def __init(self, token):
        pass

    def has_done(self):
        return self.__done

    def __finalize(self):
        self.__done = True

    def exec(self, token):
        self.state(token)