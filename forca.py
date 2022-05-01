from random import randrange
  
def jogar():
  abertura()
  print()
  print('-> Tente adivinhar a fruta que estou pensando!')
  print('-> Você pode errar 7 vezes no máximo, senão perde!')
  acertos = 0
  erro = 0
  fruta = palavra_secreta()
  letras_chutadas = []
  print()
  alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
  palavra = ['_' for x in fruta]

  
  while erro < 7 and '_' in palavra:
    print()
    for z in palavra:
      print(z, end=' ')

    print()
    chute = input('\nDigite uma letra: ').lower()
    letras_chutadas.append(chute)
    indice = 0

    
    if chute not in alfabeto.split():
      print('Você deve digitar uma letra!')

    elif letras_chutadas.count(chute) == 2:
      print('Você já digitou essa letra!')

    else:  
      if chute in fruta:
        acertos += 1
        
        for letra in fruta:
          if chute == letra:
            palavra[indice] = chute
          indice += 1
          
      else:
        erro += 1
        print('\n\nA fruta não possui a letra',chute.upper())
        desenha_forca(erro)
      

  if erro == 7:
    print("\n\nPuxa, você foi enforcado!")
    print("A palavra era {}\n".format(fruta.capitalize()))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

  else:
    print("\n\nParabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


    
def abertura():
  print('*' * 60)
  print('Bem vindo ao jogo da Forca!'.center(60))
  print('*' * 60)
    
  print("  _______     ")
  print(" |/      |    ")
  print(" |            ")
  print(" |            ")
  print(" |            ")
  print("_|___         ")
  


def palavra_secreta():
  arquivo = open('palavra.txt','r')
  lista = []
    
  for linha in arquivo:
    linha = lista.append(linha.strip())
  arquivo.close()

  aleatorio = lista[randrange(0,len(lista))]
  fruta = lista[randrange(0,len(lista))]
  return fruta


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
  jogar()
