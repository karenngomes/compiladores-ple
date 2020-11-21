from .ScopeManager import ScopeManager

class SymbolsHandler(object):
  def __init__(self):
    self.scope_manager = ScopeManager()
    self.previous_scope = ''
    self.current_scope = 'global'
    self.__next_action = self.__analyze # estado a ser executado no momento
    self.action_buffer = []

  def analyze(self, _token):
    """
    Executa a máquina de estado, recebe um token e muda o estado atual da máquina (self.__next_action)
    """
    self.__next_action(_token)

  def __analyze(self, _token):
    """
    Estado inicial e estado final da maquina de estado.
    """
    symbol, token = _token
    if symbol == 'procedure' or symbol == 'function':
      self.__next_action = self.__change_scope
    elif symbol == 'var':
      self.__next_action = self.__var_declaration

  def __change_scope(self, _token):
    """
    Estado intermediário da maquina de estado, que trata procedimento e funcao
    """
    symbol, token = _token
    self.scope_manager.create_scope(symbol)
    self.previous_scope = self.current_scope
    self.current_scope = symbol
    self.__next_action = self.__prepare_parameter_declaration
    scope = self.scope_manager[self.previous_scope]
    scope.add_entry({
      'lexema': symbol,
      'token' : token,
      'category': '',
      'scope': self.current_scope,
      'type': None,
      'value': None,
    })

  def __prepare_parameter_declaration(self, _token):
    """
    Estado intermediário da maquina de estado, que prepara para receber os parametros, caso haja
    """
    if _token[0] == '(':
      self.__next_action = self.__parameter_declaration
    elif _token[0] == ':':  # se entrar significa que é uma função que não tem parametros
      self.__next_action = self.__get_function_type
    else: # procedimento sem parametros
      self.__next_action = self.__end_routine
  
  def __parameter_declaration(self, _token):
    """
    Estado intermediário da maquina de estado, que trata declaração de parametros
    """
    self.__var_declaration(_token) # trata a declaração de variaveis dentro dos parametros
    if _token[0] == ':': # se terminou a declaracao das variaveis, altera o estado de get_var_type para get_parameters_type
      self.__next_action = self.__get_parameters_type # seta o tipo das variaveis declaradas
  
  def __get_parameters_type(self, _token):
    if _token[0] == ';':
      self.__next_action = self.__parameter_declaration
    elif _token[0] == ')':
      self.__next_action == self.__end_routine
    else:  # li o tipo do argumento
      self.__get_var_type(_token)
      self.__next_action = self.__get_parameters_type
  def __end_routine(self, _token):
    scope = self.scope_manager[self.previous_scope]  # nome do escopo onde a rotina está sendo declarada
    entry = scope[self.current_scope]  # o escopo atual tem o mesmo nome da rotina
    if _token[0] == ';': # so pode ser procedimento
      entry['category'] = 'procedure'
    elif _token[0] == ':': #so poder ser funcao
      entry['category'] = 'function'
      entry['type'] = 'integer' # todas as funcoes sao inteiras
    self.__next_action = self.__analyze

  def __var_declaration(self, _token):
    """
    Estado intermediário da maquina de estado, que trata declaracao de variaveis normais
    """
    symbol, token = _token
    if symbol == ',':
      return
    elif symbol == ':':
      self.__next_action = self.__get_var_type
    else: # li <id>
      scope = self.scope_manager[self.current_scope]
      self.action_buffer.append(
        (scope.add_entry, {
          'lexema': symbol,
          'token' : token,
          'category': 'variable',
          'scope': self.current_scope,
          'type': None,
          'value': None,
        })
      )

  def __get_var_type(self, _token):
    """
    Estado intermediário da maquina de estado, que trata declaração do tipo das variaveis
    """
    symbol = _token[0]
    while len(self.action_buffer) > 0:
      function, arg = self.action_buffer.pop() #
      arg['type'] = symbol #
      function(arg) #
    self.__next_action = self.__analyze