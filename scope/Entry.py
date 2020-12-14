
class Entry(object):
  def __init__(self, lexema, token, category, 
               scope, _type, value=None):
    self.lexema = lexema
    self.token = token
    self.category = category
    self.scope = scope
    self.type = _type
    self.value = value

  def __str__(self):
    value = self.value
    _type = self.type
    if value is None:
      value = 'None'
    if _type is None:
      _type = 'None'
    
    return f'{self.lexema:^15}|{self.token:^15}|{self.category:^15}|\
{self.scope:^15}|{_type:^15}|{value:^15}'
