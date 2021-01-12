class StatesChain(object):
    def __init__(self, scope_manager, token_list, index, state=None):
        self.scope_manager = scope_manager
        self.state = state
        self.token_list = token_list
        self.index = index
        self.__done = False # determina se o ramo da maquina de estado chegou num estado final

    def __begin(self, token):
        pass

    def has_done(self):
        return self.__done

    def _finalize(self):
        self.__done = True

    def run(self, token):
        return self.state(token)

    def exec(self):
        while True:
            value = self.run(self.token_list[self.index[0]])
            if self.has_done(): break
            self.index[0] += 1
        return value
