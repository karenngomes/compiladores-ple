from sys import path as sys_path
from utils import Path

sys_path.append(str(Path().script_dir()))

from LexicalAnalyzer import Lexical
from SyntaticAnalyzer import Syntatic


def main():
  with open('teste.pas', 'r') as file:
    tokens = Lexical(file).split()
    print('\n\n', tokens, '\n\n')
    parser_return = Syntatic(tokens).parse()


if __name__ == '__main__':
  main()




