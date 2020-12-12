
class SymbolsTable(object):
  def __init__(self, scope):
    self.items = {} # tabela de simbolos
    self.scope = scope # escopo dessa tabela
  
  def add_entry(self, item): 
    """
    adiciona um item a tabela de simbolos
    item: item que iremos adicionar
    obs.: informações sobre item está em SymbolsHandler
    """
    name = item['lexema'] 
    if name in self.items.keys():
      raise Exception(f'DuplicatedIdentifierError: Identifier {name} duplicated.')
    self.items[name] = item
  
  def values(self):
    return self.items.values
  
  def __getitem__(self, key):
    return self.items[key]
