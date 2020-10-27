from Alphabet import Alphabet


class Lexical(object):

  def __init__(self, file):
    self.file = file
    self.tokens = []
    self.buffer = ''
    self.line = 0
    self.pos = 0
    self.alphabet = Alphabet()

  def __handle_buffer(self):
    if len(self.buffer) > 0 and self.alphabet.is_number(self.buffer): # se for um numero
      self.tokens.append((self.buffer, 'intnum'))
    elif len(self.buffer) > 0 and self.alphabet.is_word(self.buffer): # se for palavra
      if self.alphabet.is_boolean_one(self.buffer): # verifica se eh op boolean1
        self.tokens.append((self.buffer, 'boolean1'))
      elif self.alphabet.is_boolean_two(self.buffer): # verifica se eh op boolean2
        self.tokens.append((self.buffer, 'boolean2'))
      elif self.alphabet.is_reserved_word(self.buffer): # ou se eh palavra reservada
        self.tokens.append((self.buffer, 'reserved'))
      else: # entao eh um identificador
        self.tokens.append((self.buffer, 'id'))
    self.buffer = ''

  def __is_compose_delimiter(self, line_buffer):
    current_symbol = line_buffer[self.pos]
    if self.pos + 1 < len(line_buffer): 
      compose = current_symbol + line_buffer[self.pos + 1]
      if self.alphabet.is_compose_delimiter(compose): 
        if self.alphabet.is_relational(compose):
          self.tokens.append((compose, 'relational'))
        else:
          self.tokens.append((compose, 'delimiter'))
        self.pos += 1
        return True
    return False
          
  def __split(self, line_buffer):
    current_symbol = line_buffer[self.pos]
    if self.alphabet.is_white_space(current_symbol):
      self.__handle_buffer()

    elif self.alphabet.is_delimiter(current_symbol):
      self.__handle_buffer()
      if not self.__is_compose_delimiter(line_buffer):
        if self.alphabet.is_operator(current_symbol):
          self.tokens.append((current_symbol, 'operator'))
        else:
          self.tokens.append((current_symbol, 'delimiter'))

    elif self.alphabet.has(current_symbol): 
      self.buffer += current_symbol

    else:
      raise Exception(f'Invalid symbol at position {self.pos + 1}, line {self.line}')

  def split(self):
    while True:
      line_buffer = self.file.readline()
      if line_buffer == '': break
      self.line += 1
      while (self.pos < len(line_buffer)):
        self.__split(line_buffer)
        self.pos += 1
      self.pos = 0
    return self.tokens


