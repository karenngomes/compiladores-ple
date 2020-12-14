import pytest
from scope import ScopeManager, SymbolsTable, Entry

def test_create_scope():
    sm = ScopeManager()
    a = sm.create_scope('teste1')
    assert sm['teste1'] == a


def test_stack():
    sm = ScopeManager()
    a = sm.create_scope('teste1', register=False, push=True)
    assert a == sm.get_stack_top()
    assert a.scope_name == sm.get_stack_top_name()
    assert a == sm.pop_stack()
    sm.pop_stack()
    assert sm['global'] == sm.pop_stack()


def test_get_in_stack_from_top():
    sm = ScopeManager()
    a = sm.create_scope('teste1', push=True)
    b = sm.create_scope('teste2', push=True)
    assert sm.get_in_stack_from_top(1) == a
    assert sm.get_in_stack_from_top(2) == sm['global']


def test_search_identifier():
    sm = ScopeManager()
    _global = sm['global']
    g1 = Entry('gvar1', 'id', 'variable', 'global', 'integer', 3)
    g2 = Entry('var2', 'id', 'variable', 'global', 'integer', 4)
    _global.add_entry(g1)
    _global.add_entry(g2)

    a = sm.create_scope('es1', push=True)
    a1 = Entry('var1', 'id', 'variable', 'es1', 'boolean', 1)
    a2 = Entry('var2', 'id', 'variable', 'es1', 'integer', 5)
    a.add_entry(a1)
    a.add_entry(a2)

    b = sm.create_scope('es2', push=True)
    b1 = Entry('var1', 'id', 'variable', 'es1', 'boolean', 1)
    b.add_entry(b1)

    id = sm.search_identifier('var1')
    print(id)
    assert id == b1
    id = sm.search_identifier('var2')
    print(id)
    assert id == a2
    id = sm.search_identifier('gvar1')
    print(id)
    assert id == g1
                