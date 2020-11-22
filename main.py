from sys import path as sys_path, argv
from utils import Path

main_path = str(Path().script_dir())
sys_path.append(main_path)

from LexicalAnalyzer import Lexical
from SyntaticAnalyzer import Syntatic


if main_path[len(main_path) - 1] != '/':
      main_path += '/'


def main():
  file = argv[1] if len(argv) > 1 else main_path +'teste.pas'
  with open(file, 'r') as file:
    tokens = Lexical(file).split()
    print('Análise Léxica bem sucedida. A lista de tokens gerados está disponível no arquivo tokens.log')
    print_tokens(tokens)
    #print('\n\n', tokens, '\n\n')
    symbols_table = Syntatic(tokens).parse()
    print('Análise Sintática bem sucedida. A tabela de símbolos  está disponível no arquivo symbols-table.log')
    print_table(symbols_table)


def print_tokens(tokens):
  with open(main_path + 'tokens.log', 'w') as log:
    log.write(str(tokens))


def print_table(table):
  buffer = ''
  scopes = table.scopes
  for scope in scopes.values():
    table_items = scope.items
    if len(table_items) == 0:
      continue
    columns_names = list(table_items.values())[0].keys()
    for column in columns_names: # imprime uma linha com o nome das colunas
      buffer += f'{column:-^16}'
    buffer += '\n'
    for entry in table_items.values():
      for column in entry.keys():
        if entry[column] is not None:
          buffer += f'{entry[column]: ^15}|'
        else:
          mock = 'None'
          buffer += f'{mock: ^15}|'
      buffer += '\n'
    buffer += '\n'

  with open(main_path + 'symbols-table.log', 'w') as log:
    log.write(buffer)



if __name__ == '__main__':
  main()  




