import pytest
from semanthicanalyzer.states import ExpressionChain
from scope import ScopeManager, Entry

# a + 2 * 4 - b / c
token_list = [['a', 'id'], ['+', 'operador'], ['2', 'intnum'],
              ['*', 'operador'], ['0', 'intnum'], ['-', 'operador'],
              ['b', 'id'], ['/', 'operador'], ['c', 'id'], [';', 'delimiter']
             ]

sm = ScopeManager()
gbl = sm['global']
# 5 + 2 * 0 - 200 // 3 = -4
gbl.add_entry(Entry('a', 'id', 'variable', 'global', 'integer', 5))
gbl.add_entry(Entry('b', 'id', 'variable', 'global', 'integer', 10))
gbl.add_entry(Entry('c', 'id', 'variable', 'global', 'integer', 3))


def test_expression():
    index = [[0], [0]]
    exp_chain = ExpressionChain(sm, token_list, index[0])
    exp_chain2 = ExpressionChain(sm, [['4', 'intnum'],[';', 'delimiter']],
                                 index[1])
    exp_chain3 = ExpressionChain(sm, [['a', 'id'], ['to', 'reserved']],
                                 index[1])        

    value = exp_chain.exec()
    value2 = exp_chain2.exec()
    value3 = exp_chain3.exec()
    assert value == -4 
    assert value2 == 4
    assert value3 == 5