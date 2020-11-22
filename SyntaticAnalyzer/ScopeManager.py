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

  def push_in_stack(self, scope):
    self.scope_stack.append(scope)
  
  def pop_stack(self):
    if len(self.scope_stack) == 1: # caso so reste o escopo global na pilha
      return self.scope_stack[0]
    return self.scope_stack.pop()

  def get_stack_top_name(self):
    top = self.scope_stack[len(self.scope_stack) - 1]
    return top.scope
  
  def get_stack_top(self):
    top = self.scope_stack[len(self.scope_stack) - 1]
    return top
  
  def get_in_stack_from_top(self, index):
    top = self.scope_stack[len(self.scope_stack) - 1 - index]
    return top
