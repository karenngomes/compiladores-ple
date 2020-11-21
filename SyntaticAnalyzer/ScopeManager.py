from .SymbolsTable import SymbolsTable

class ScopeManager(object):
  def __init__(self):
    self.scopes = {'global': SymbolsTable('global')}
    self.scope_stack = [self.scopes['global']]

  def create_scope(self, name):
    self.scopes[name] = SymbolsTable(name)
    return self.scopes[name] 

  def __getitem__(self, key):
    return self.scopes[key]
