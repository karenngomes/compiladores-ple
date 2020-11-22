import csv, sys
from .SymbolsHandler import SymbolsHandler

class Syntatic(object):
  special_terminals = ['intnum', 'id', 'relacao', 'operador', 'boolean1', 'boolean2']

  terminals = ['$', ',', ';', ':=', ':', '.', '(', ')','program', 'begin', 'end', 'var', 
  'integer', 'boolean', 'procedure', 'function', 'read', 'write', 'for', 'to', 'do', 
  'repeat', 'until', 'while', 'if', 'then','else']

  def __init__(self, tokens):
    self.tokens = tokens
    self.tokens.append(('$', 'end'))
    self.current_token = 0
    self.syntatic_table = self.__read_table()
    self.symbols_table = None
    self.symbols_handler = SymbolsHandler()
    self.stack = ['$', '<programa>']

  def stack_pop(self):
    return self.stack.pop()
  
  def stack_push(self, item):
    if type(item) == type([]):
      for i in item:
        self.stack.append(i)
    else:
      self.stack.append(item)

  def parse(self):
    while(len(self.stack) > 0):
      #print(self.stack, end='    ')
      top = self.stack_pop()
      current = self.tokens[self.current_token]
      #print(f'current: {current[0]}')
      if self.match(top, current):
        self.current_token += 1
        self.symbols_handler.analyze(current)
      elif self.is_non_terminal(top):
        self.__expand_production(top, current)
      else:
        raise Exception(f'SyntaticError: Expecting {top[0]}, got {current[0]}.')
    self.symbols_table = self.symbols_handler.scope_manager
    return self.symbols_table

  def is_non_terminal(self, top):
    return top[0] == '<' and top[len(top) - 1] == '>'
  
  def __expand_production(self, top, current):
    production = self.__get_production(top, current)
    if production == '':
      raise Exception('SyntaticError.')
      #print(self.stack)
      #print('erro')
      #sys.exit(0)
    elif production == '#':
      pass
    else:
      production = production.split(' ')[::-1]
      self.stack_push(production)

  def __get_production(self, top, current):
    column = current[0]
    if current[1] in self.special_terminals:
      column = current[1]
    return self.syntatic_table[top][column]


  def match(self, top, current):
    # ('temp', 'id')
    if current[1] in self.special_terminals:
      if top[0] == '<':  #and top not in ['<=', '<']:
        size = len(top) - 1
        return top[1:size] == current[1]
      else:
        return False
    return top in self.terminals

  def __read_table(self):
    with open('SyntaticAnalyzer/syntatic-table.csv') as csvfile:
      table = csv.DictReader(csvfile)
      temp = list(table)
      table = self.__format_table(temp)
      return table

  def __format_table(self, csv_table):
    my_dict = {}
    for row in csv_table:
      line_label = row['producoes']
      my_dict[line_label] = row
      temp = my_dict[line_label]
      del temp['producoes']
      self.__replace_comma(temp)
    return my_dict

  def __replace_comma(self, row):
    row[','] = row['|']
    del row['|']
    row[','] = row[','].replace('|', ',')



if __name__ == '__main__':
  # read_table()
  pass
