from sys import path as sys_path
from utils import Path

sys_path.append(str(Path().script_dir()))

from LexicalAnalyzer import Lexical
from SyntaticAnalyzer import Syntatic


def main():
  with open('teste.pas', 'r') as file:
    tokens = Lexical(file).split()
    print('\n\n', tokens, '\n\n')
    symbols_table = Syntatic(tokens).parse()
    print_table(symbols_table)


def print_table(table):
  scopes = table.scopes
  for scope in scopes.values():
    table_items = scope.items
    columns_names = list(table_items.values())[0].keys()
    for column in columns_names: # imprime uma linha com o nome das colunas
      print(f'{column:-^11}', end='')
    print()
    for entry in table_items.values():
      for column in entry.keys():
        if entry[column] is not None:
          print(f'{entry[column]: ^10}', end='|')
        else:
          mock = 'None'
          print(f'{mock: ^9}', end='|')
      print() 



if __name__ == '__main__':
  main()




