from Lexical import Lexical

def main():
  with open('teste.pas', 'r') as file:
    analizer = Lexical(file)
    print(analizer.split())


if __name__ == '__main__':
  main()