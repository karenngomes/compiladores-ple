import pytest
from semanthicanalyzer.states import IfChain
from scope import ScopeManager, Entry

token_list = [['if', 'reserved', 12], ['(', 'delimiter'], ['entrada', 'id'],
              ['>', 'relacao'], ['aux', 'id'], [')', 'delimiter'], ['then', 'reserved'], 
              ['begin', 'reserved'],
                    ['aux', 'id'], [':=', 'attribution'], ['5', 'intnum'], [';', 'delimiter'],
              ['end', 'reserved'],
              ['else', 'reserved'], ['begin', 'reserved'],
                    ['aux', 'id'], [':=', 'attribution'], ['10', 'intnum'], [';', 'delimiter'],
              ['end', 'reserved'], [';', 'delimiter']]

sm = ScopeManager()
glb = sm['global']
e1 = Entry('entrada', 'id', 'variable', 'global', 'integer', 10)
e2 = Entry('aux', 'id', 'variable', 'global', 'integer', 0)

glb.add_entry(e1)
glb.add_entry(e2)

def test_if():
    index = [[0], [0]]
    if_chain = IfChain(sm, token_list, index[0])
    if_chain2 = IfChain(sm, token_list, index[1])

    if_chain.exec()
    e1.value = -10
    if_chain2.exec()

    assert index[0] == 6
    assert index[1] == 12