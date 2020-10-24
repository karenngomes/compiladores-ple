import re


class Alphabet(object):
  def __init__(self):
    self.alphabet_pattern = re.compile(r'^[a-zA-Z\d]$')
    self.word_pattern = re.compile(r'^[a-zA-Z\d]*$')
    self.delimiter_pattern = re.compile(r'^[:;,()+\-*/=><]$')
    self.white_space_pattern = re.compile(r'[ \n\t]')
    self.compose_delimiter_pattern = re.compile(r'^[:<>]=$|^[=<]>$')
  
  def is_word(self, string : str) -> bool:
    return bool(self.word_pattern.match(string))

  def is_number(self, string : str) -> bool:
    return bool(string.isdigit())

  def is_delimiter(self, string : str) -> bool:
    return  bool(self.delimiter_pattern.match(string))

  def is_compose_delimiter(self, string : str) -> bool:
    return bool(self.compose_delimiter_pattern.match(string))

  def is_white_space(self, string : str) -> bool:
    return bool(self.white_space_pattern.match(string))

  def has(self, symb : str) -> bool:
    return bool(self.alphabet_pattern.match(symb))

if __name__ == '__main__':
  alp = Alphabet()
  print(alp.is_word('a1'))