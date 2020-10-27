from Lexical import Lexical

if __name__ == '__main__':
  with open('teste.pas', 'r') as file:
    analizer = Lexical(file)
    print(analizer.split())