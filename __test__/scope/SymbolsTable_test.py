import pytest
from scope import SymbolsTable, Entry


def test_add_entry():
  st = SymbolsTable('testing')
  e = Entry('var1', 'id', 'variable', 'testing', 'integer', None)
  st.add_entry(e)

  b = st['var1']

  assert st['var1'] == e


def test_entry_exists():
  st = SymbolsTable('testing')
  e = Entry('var1', 'id', 'variable', 'testing', 'integer', None)
  st.add_entry(e)

  result = st.entry_exists('var1')

  assert result == True
