import re


class Alphabet(object):
  def __init__(self):
    self.alphabet_pattern = re.compile(r'^[a-zA-Z\d]$')
    self.word_pattern = re.compile(r'^[a-zA-Z\d]*$')
    self.delimiter_pattern = re.compile(r'^[:;,()+\-*/=><]$')
    self.white_space_pattern = re.compile(r'[ \n\t]')
    self.compose_delimiter_pattern = re.compile(r'^[:<>]=$|^[=<]>$')
    self.booleans_one = ['and', 'or']
    self.booleans_two = ['not']
    self.reserved_words = ['program', 'begin', 'end', 'var', 'integer', 'boolean', 'procedure', 'function', 'read', 'write', 'for', 'to', 'do', 'repeat', 'until', 'while', 'if', 'then','eles']
    self.relationals = ['<', '>', '=', '<>', '<=', '>=']
    self.operators = ['+', '-', '*', '/']
    
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
  
  def is_boolean_one(self, string : str) -> bool:
    return string in self.booleans_one
  
  def is_boolean_two(self, string : str) -> bool:
    return string in self.booleans_two
    
  def is_reserved_word(self, string : str) -> bool:
    return string in self.reserved_words
  
  def is_relational(self, string : str) -> bool:
    return string in self.relationals
    
  def is_operator(self, string : str) -> bool:
    return string in self.operators
  
  def has(self, symb : str) -> bool:
    return bool(self.alphabet_pattern.match(symb))
