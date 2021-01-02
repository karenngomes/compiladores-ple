class StatesChain(object):
    def __init__(self, scope_manager):
        self.scope_manager = scope_manager
        self.__done = False # determina se o ramo da maquina de estado chegou num estado final
    
    def __begin(self, token):
        pass

    def has_done(self):
        return self.__done

    def _finalize(self):
        self.__done = True

    def run(self, token):
        return self.state(token)