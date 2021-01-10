import pytest
from semanthicanalyzer.states import ExpressionChain
from scope import ScopeManager, Entry

# a + 2 * 4 - b / c
token_list = [['a', 'id'], ['+', 'operador'], ['2', 'intnum'],
              ['*', 'operador'], ['0', 'intnum'], ['-', 'operador'],
              ['b', 'id'], ['/', 'operador'], ['c', 'id'], [';', 'delimiter']
             ]
token_list2 = [['d', 'id'], [';', 'delimiter']]
token_list3 = [['d', 'id'], ['+', 'operador'], ['2', 'intnum'], [';', 'delimiter']]
token_list4 = [['2', 'intnum'], ['+', 'operador'], ['d', 'id'], [';', 'delimiter']]

sm = ScopeManager()
gbl = sm['global']
# 5 + 2 * 0 - 200 // 3 = -4
gbl.add_entry(Entry('a', 'id', 'variable', 'global', 'integer', 5))
gbl.add_entry(Entry('b', 'id', 'variable', 'global', 'integer', 10))
gbl.add_entry(Entry('c', 'id', 'variable', 'global', 'integer', 3))
gbl.add_entry(Entry('d', 'id', 'variable', 'global', 'boolean', 1))


def test_expression():
    index = [[0], [0], [0], [0], [0]]
    exp_chain = ExpressionChain(sm, token_list, index[0])
    exp_chain2 = ExpressionChain(sm, [['4', 'intnum'],[';', 'delimiter']],
                                 index[1])
    exp_chain3 = ExpressionChain(sm, token_list2, index[2])
    exp_chain4 = ExpressionChain(sm, token_list3, index[3])
    exp_chain5 = ExpressionChain(sm, token_list4, index[4])

    value = exp_chain.exec()
    value2 = exp_chain2.exec()
    value3 = exp_chain3.exec()

    assert value == -4
    assert value2 == 4
    assert value3 == 1
    with pytest.raises(Exception):
        value4 = exp_chain4.exec()
        value5 = exp_chain5.exec()
