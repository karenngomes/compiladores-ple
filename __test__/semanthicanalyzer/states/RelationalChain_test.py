import pytest
from semanthicanalyzer.states import RelationalChain
from scope import ScopeManager, Entry

token_list = [['a', 'id'], ['>', 'relational'], 
             ['3', 'intnum'], [';', 'delimiter']]
token_list2 = [['a', 'id'], ['+', 'operator'], ['2', 'intnum'],
              ['=', 'relational'], ['3', 'intnum'], 
              [';', 'delimiter']]

sm = ScopeManager()
glb = sm['global']
a = Entry('a', 'id', 'variable', 'global', 'integer', 1)
glb.add_entry(a)


def test_relational():
    index = [[0], [0]]
    rel_chain = RelationalChain(sm, token_list, index[0])
    rel_chain2 = RelationalChain(sm, token_list2, index[1])

    value = rel_chain.exec()
    value2 = rel_chain2.exec()

    assert value == False
    assert value2 == True