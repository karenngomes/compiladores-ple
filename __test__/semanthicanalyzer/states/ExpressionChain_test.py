import pytest
from semanthicanalyzer.states import ExpressionChain
from scope import ScopeManager, Entry

# a + 2 * 4 - b / c
token_list = [['a', 'id'], ['+', 'operator'], ['2', 'intnum'],
              ['*', 'operator'], ['0', 'intnum'], ['-', 'operator'],
              ['b', 'id'], ['/', 'operator'], ['c', 'id'], [';', 'delimiter']
             ]

sm = ScopeManager()
gbl = sm['global']
# 5 + 2 * 0 - 200 // 3 = -4
gbl.add_entry(Entry('a', 'id', 'variable', 'global', 'integer', 5))
gbl.add_entry(Entry('b', 'id', 'variable', 'global', 'integer', 10))
gbl.add_entry(Entry('c', 'id', 'variable', 'global', 'integer', 3))


def test_chain():
    index = [0]
    exp_chain = ExpressionChain(sm, token_list, index)
    value = exp_chain.exec()
    
    assert value == -4 