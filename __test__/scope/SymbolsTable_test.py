import pytest
from sys import path as sys_path
from utils import Path


from scope import SymbolsTable, Entry


def test_add_entry():
  st = SymbolsTable('testing')
  e = Entry('var1', 'id', 'variable', 'testing', 'integer', None)
  st.add_entry(e)
  assert st['var1'] == e


def test_entry_exists():
  st = SymbolsTable('testing')
  e = Entry('var1', 'id', 'variable', 'testing', 'integer', None)
  st.add_entry(e)
  assert st.entry_exists('var1') == True