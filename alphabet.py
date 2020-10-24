import re


class Alphabet(object):
  def __init__(self):
    self.word_pattern = re.compile(r'^[a-zA-Z][a-zA-Z\d]*$')
    self.delimiter_pattern = re.compile(r'^[:;,()+\-*/=><]$')
    #self.compose_delimiter_pattern = re.compile(r'^[:<>]=$|^[=<]>$')
  
  def is_word(self, string : str) -> bool:
    return self.word_pattern.match(string)

  def is_number(self, string : str) -> bool:
    return string.digit(string)

  def is_delimiter(self, string : str) -> bool:
    return  self.delimiter_pattern.match(string)