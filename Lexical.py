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
    if len(self.buffer) > 0 and self.alphabet.is_number(self.buffer):
      self.tokens.append((self.buffer, 'number'))
    elif len(self.buffer) > 0 and self.alphabet.is_word(self.buffer):
      self.tokens.append((self.buffer, 'word'))
    self.buffer = ''

  def __is_compose_delimiter(self, line_buffer):
    current_symbol = line_buffer[self.pos]
    if self.pos + 1 < len(line_buffer): 
      compose = current_symbol + line_buffer[self.pos + 1]
      if self.alphabet.is_compose_delimiter(compose): 
        self.tokens.append((compose, 'compose_delimiter'))
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
        self.tokens.append((current_symbol, 'simple_delimiter'))

    elif self.alphabet.has(current_symbol): 
      self.buffer += current_symbol

    else:
      raise Exception(f'Invalid symbol at position {oself.pos + 1}, line {self.line}')

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


if __name__ == '__main__':
  with open('teste.pas', 'r') as file:
    analizer = Lexical(file)
    print(analizer.split())

