#VERSÃO FINAL:

!pip install colorama

from types import NoneType #Importa lib de NoneType para evitar Enter's indevidos
import time #Importa lib para a def loading()
from IPython.display import clear_output #Importa lib para limpar console
from colorama import Fore , Style #Importa lib para colorir o console

#Define uma matriz com todos os navios do jogo
NAVIOS = [
    ['Porta-aviões' , 5] ,
    #['Encouraçado' , 4] ,
    #['Cruzador' , 3] ,
    #['Submarino' , 3] ,
    ['Destroyer' , 2] ,
]

#Define os caracteres que serão impressos no terminal
NAVIO = 'O'
AGUA = f'{Fore.CYAN}{Style.BRIGHT}­­­­­­≈{Style.RESET_ALL}' #Fore.x = Define a cor do texto , Style.BRIGHT = ressalta a cor do texto
ERRO = f'{Fore.RED}­­­­­­­­­­­­­­­­­­­­­X{Style.RESET_ALL}'
ACERTO = f'{Fore.GREEN}{Style.BRIGHT }#{Style.RESET_ALL}' #Style.RESET_ALL = Define onde a colaração do texto termina

def limparConsole():
  clear_output(wait=True) #Limpa o console mas só depois de um input com wait=True

def loading():
  print("CARREGANDO[" , end="" , flush=True)

  for _ in range (6):
    print("▰" , end="" , flush=True) #end="" impede que o print quebre linha de exibição em exibição
    time.sleep(0.3)

  for _ in range (17):
    print("▰" , end="" , flush=True) #flush=True força o buffer descarregar o armazanemento e exibir o print sequencialmente mesmo em intervalos de tempo pequenos
    time.sleep(0.2)

  print("]")

def criarTabuleiro():
  tabuleiro = [] #Cria uma lista vazia

  for linhas in range(10):
    linha_tab = [] #Linhas do tabuleiro que serão criadas 10 vezes

    for colunas in range(10):
      linha_tab.append(AGUA) #Incrementa o caracter de água nas linhas por 10 vezes

    tabuleiro.append(linha_tab) #Adciona a linha com AGUA na matriz tabuleiro

  return tabuleiro

def imprimirTabuleiro(tab, ocultar=False , J1=False): #Ocultar = True e J1 = False é o parâmetro padrão da função

  if J1 == True: #Pinta o tabuleiro de vermelho caso seja o tabuleiro do J1
    print(f'{Fore.RED}{Style.BRIGHT}{"=" * 32}{Style.RESET_ALL}' , end = f"\t\t\t{Fore.MAGENTA}{Style.BRIGHT}Legenda:{Style.RESET_ALL}\n")
    print(f'{Fore.RED}{Style.BRIGHT}   1  2  3  4  5  6  7  8  9  10{Style.RESET_ALL}' , end = f"\t\t\t{Fore.CYAN}{Style.BRIGHT}≈{Style.RESET_ALL} = {Fore.CYAN}{Style.BRIGHT}Água{Style.RESET_ALL}\n")

  else: #Pinta o tabuleiro de azul caso seja o tabuleiro do J2
    print(f'{Fore.BLUE}{Style.BRIGHT}{"=" * 32}{Style.RESET_ALL}' , end = f"\t\t\t{Fore.MAGENTA}{Style.BRIGHT}Legenda:{Style.RESET_ALL}\n")
    print(f'{Fore.BLUE}{Style.BRIGHT}   1  2  3  4  5  6  7  8  9  10{Style.RESET_ALL}' , end = f"\t\t\t{Fore.CYAN}{Style.BRIGHT}≈{Style.RESET_ALL} = {Fore.CYAN}{Style.BRIGHT}Água{Style.RESET_ALL}\n")


  letras = 'ABCDEFGHIJ' #Lista de letras para as linhas

  celulas = [] #Cria uma matriz vazia para tratar os elementos do tabuleiro

  for lin in range(len(tab)):
    linhaCel = []

    for cel in range(len(tab)):

      celula = tab[lin][cel]

      if ocultar == True and celula == NAVIO:
        linhaCel.append(AGUA)

      else:
        linhaCel.append(celula)

    celulas.append(linhaCel)

  for i in range(10):
    linha_cel = celulas[i]

    if i == 0:
      if J1 == True: #Imprime a letra da linha em vermelho para o J1
        print(f'{Fore.RED}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = "\t\t\t\tO = Navio\n")

      else: #Imprime a letra da linha em azul para o J2
        print(f'{Fore.BLUE}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = "\t\t\t\tO = Navio\n")

    elif i == 1:
      if J1 == True:
        print(f'{Fore.RED}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = f"\t\t\t\t{Fore.GREEN}{Style.BRIGHT}#{Style.RESET_ALL} = {Fore.GREEN}{Style.BRIGHT}Acerto{Style.RESET_ALL}\n")

      else:
        print(f'{Fore.BLUE}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = f"\t\t\t\t{Fore.GREEN}{Style.BRIGHT}#{Style.RESET_ALL} = {Fore.GREEN}{Style.BRIGHT}Acerto{Style.RESET_ALL}\n")

    elif i == 2:
      if J1 == True:
        print(f'{Fore.RED}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = f"\t\t\t\t{Fore.RED}{Style.BRIGHT}X{Style.RESET_ALL} = {Fore.RED}{Style.BRIGHT}Erro{Style.RESET_ALL}\n")

      else:
        print(f'{Fore.BLUE}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel) , end = f"\t\t\t\t{Fore.RED}{Style.BRIGHT}X{Style.RESET_ALL} = {Fore.RED}{Style.BRIGHT}Erro{Style.RESET_ALL}\n")

    else:
      if J1 == True:
        print(f'{Fore.RED}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel))

      else:
        print(f'{Fore.BLUE}{Style.BRIGHT}{letras[i]}{Style.RESET_ALL}  ' + '  '.join(linha_cel))


  if J1 == True:
    print(f'{Fore.RED}{Style.BRIGHT}{"=" * 32}{Style.RESET_ALL}')

  else:
    print(f'{Fore.BLUE}{Style.BRIGHT}{"=" * 32}{Style.RESET_ALL}')


def converterCoordenadas(coord):
  coord = coord.strip().upper()
  letras_conv = 'ABCDEFGHIJ'

  if len(coord) < 2 or len(coord) > 3:
    return None

  letra = coord[0]
  numero = coord[1:]

  flag = 0
  for k in range(len(letras_conv)):
    if letra == letras_conv[k]:
      flag = 1

  if flag == 0:
    return None

  if coord is NoneType:
    return None

  try:
    coluna_conv = int(numero) - 1

  except ValueError:
    return None

  linha_conv = letras_conv.index(letra)

  if coluna_conv < 0 or coluna_conv > 9:
    return None

  return [linha_conv , coluna_conv]

def posicionarNavios(tab , nome , jogador):

  navios_jogador = []

  print('')
  if jogador == 1:
    print(f"\nPosicionamento dos navios de {Fore.RED}{Style.BRIGHT}{nome}{Style.RESET_ALL}")
    imprimirTabuleiro(tab , J1=True)
  else:
    print(f"\nPosicionamento dos navios de {Fore.BLUE}{Style.BRIGHT}{nome}{Style.RESET_ALL}")
    imprimirTabuleiro(tab)

  for dados in range(len(NAVIOS)):
    nome_navio = NAVIOS[dados][0]
    tamanho = NAVIOS[dados][1]

    while True:

      print(f"{Fore.YELLOW}{Style.BRIGHT}\nPosicionando {nome_navio}{Style.RESET_ALL}\n⮩Tamanho: {tamanho} posições")

      coord_posi = converterCoordenadas(input('\nDigite a posição desejada. (Ex. A1): '))

      while coord_posi is None:
        print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nCoordenada inválida! Tente novamente")
        coord_posi = converterCoordenadas(input('\nDigite a posição desejada. (Ex. A1): '))

      orientacao = input("\nHorizontal = H\nVertical = V\nDigite a orientação do seu navio: ").upper()

      while orientacao not in ('H' , 'V'):
        print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nOpção inválida! Tente novamente")
        orientacao = input("\nHorizontal = H\nVertical = V\nDigite a orientação do seu navio: ").upper()

      if orientacao == 'H':
        direcao_H = input("\nEsquerda = L\nDireita = R\nDigite a direção do seu navio na horizontal: ").upper()

        while direcao_H not in ('R' , 'L'):
          print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nOpção inválida! Tente novamente")
          direcao_H = input("\nEsquerda = L\nDireita = R\nDigite a direção do seu navio na horizontal: ").upper()

      else:
        direcao_V = input("\nCima = U\nBaixo = D\nDigite a direção do seu navio na vertical: ").upper()

        while direcao_V not in ('D' , 'U'):
          print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nOpção inválida! Tente novamente")
          direcao_V = input("\nCima = U\nBaixo = D\nDigite a direção do seu navio na vertical: ").upper()

      linha_posi = coord_posi[0]
      coluna_posi = coord_posi[1]

      posicoes = []

      for a in range(tamanho):
        if orientacao == 'H':
          if direcao_H == 'R':
            posicoes.append([linha_posi , coluna_posi + a])
          else:
            posicoes.append([linha_posi , coluna_posi - a])

        else:
          if direcao_V == 'U':
            posicoes.append([linha_posi - a , coluna_posi])
          else:
            posicoes.append([linha_posi + a , coluna_posi])

      validar = 0

      for p in range(len(posicoes)):
        pos = posicoes[p]
        lin_in = pos[0]
        col_in = pos[1]

        if lin_in > 9 or lin_in < 0 or col_in > 9 or col_in < 0:
          print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nNavio não cabe nessa posição!")
          validar = 1
          break

        if tab[lin_in][col_in] != AGUA:
          validar = 1
          print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nJá existe um navio nessa posição!")
          break

      if validar == 0:

        for pi in range(len(posicoes)):
          pos = posicoes[pi]
          lin_pos = pos[0]
          col_pos = pos[1]

          tab[lin_pos][col_pos] = NAVIO

        navios_jogador.append(posicoes)
        print('')
        if jogador == 1:
          imprimirTabuleiro(tab , J1=True)

        else:
           imprimirTabuleiro(tab)

        break

  return navios_jogador

def atacar(tab, navios, coord):
  linha_atq = coord[0]
  coluna_atq = coord[1]

  if tab[linha_atq][coluna_atq] != NAVIO:
      tab[linha_atq][coluna_atq] = ERRO
      return 0

  else:
    tab[linha_atq][coluna_atq] = ACERTO

  navio_atacado = 1

  for n in range (len(navios)):
    navio = navios[n]

    for t in range(len(navio)):
      if linha_atq == navio[t][0] and coluna_atq == navio[t][1]:
        navio_atacado = navio
        navio.pop(t)
        break

    if navio_atacado != 1:
      break

  if len(navio_atacado) == 0:
    return 2

  return 1

def verificarVitoria(navios):
  for na in range(len(navios)):
    navio_vit = navios[na]

    if len(navio_vit) > 0:
      return 0

  return 1

# ============== JOGO ==============
print(f"{Fore.MAGENTA}{Style.BRIGHT}{'=' * 13} BATALHA NAVAL {"=" * 13}{Style.RESET_ALL}\n")
loading()

press = input(f'Pressione Enter para começar')
print(f"\n{Fore.RED}{Style.BRIGHT}\nJOGADOR(A) 1{Style.RESET_ALL}")
nome_j1 = input("Digite seu nome: ")
tabuleiro_j1 = criarTabuleiro()
navios_j1 = posicionarNavios(tabuleiro_j1 , nome_j1 , 1)
limparConsole()

press = input(f'\n{nome_j1} pressione Enter para continuar')
print(f"\n{Fore.BLUE}{Style.BRIGHT}\nJOGADOR(A) 2{Style.RESET_ALL}")
nome_j2 = input("Digite seu nome: ")
tabuleiro_j2 = criarTabuleiro()
navios_j2 = posicionarNavios(tabuleiro_j2 , nome_j2 , 2)
limparConsole()

jogadas = 0
turno = 1

while True:

  if turno == 0:
    nome_vez = nome_j2
    cor_alvo = 1
    minha_cor = 2
    meu_tab = tabuleiro_j2
    tab_alvo = tabuleiro_j1
    navios_alvo = navios_j1

  else:
    nome_vez = nome_j1
    minha_cor = 1
    cor_alvo = 2
    meu_tab = tabuleiro_j1
    tab_alvo = tabuleiro_j2
    navios_alvo = navios_j2


  while True:
    limparConsole()
    press = input(f'\nPressione Enter para iniciar a jogada')

    if minha_cor == 1:
      print(f"\n➤Sua vez {Fore.RED}{Style.BRIGHT}{nome_vez}!!{Style.RESET_ALL}")
    else:
      print(f"\n➤Sua vez {Fore.BLUE}{Style.BRIGHT}{nome_vez}!!{Style.RESET_ALL}")

    print(f"\n⮩Seu tabuleiro:")
    if minha_cor == 1:
      imprimirTabuleiro(meu_tab , J1=True)
    else:
      imprimirTabuleiro(meu_tab)

    print(f"\n⮩Tabuleiro adversário:")
    if cor_alvo == 1:
      imprimirTabuleiro(tab_alvo , ocultar=True, J1=True)
    else:
      imprimirTabuleiro(tab_alvo , ocultar=True, J1=False)

    jogada = converterCoordenadas(input("\nDigite uma coordenada para atacar. (Ex. A1): "))

    while jogada is None:
      print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nCoordenada inválida! Tente novamente")
      jogada = converterCoordenadas(input("\nDigite uma coordenada para atacar. (Ex. A1): "))

    while tab_alvo[jogada[0]][jogada[1]] == ACERTO or tab_alvo[jogada[0]][jogada[1]] == ERRO:
      print(f"\n{Fore.RED}ERRO:{Style.RESET_ALL}\nVocê já atacou nessa posição! Tente novamente")
      jogada = converterCoordenadas(input("\nDigite uma coordenada para atacar. (Ex. A1): "))

    break

  resultado = atacar(tab_alvo , navios_alvo , jogada)
  jogadas += 1

  if resultado == 0:
    print(f"\n➤{Fore.RED}{Style.BRIGHT}ERROU❌{Style.RESET_ALL}")

  elif resultado == 1:
    print(f"\n➤{Fore.GREEN}{Style.BRIGHT}ACERTOU🎯{Style.RESET_ALL}")

  else:
    print(f"\n➤{Fore.YELLOW}{Style.BRIGHT}NAVIO DESTRUÍDO💥{Style.RESET_ALL}")

  print('')
  if cor_alvo == 1:
      imprimirTabuleiro(tab_alvo , ocultar=True, J1=True)

  else:
    imprimirTabuleiro(tab_alvo , ocultar=True)

  vitoria = verificarVitoria(navios_alvo)

  if vitoria == 1:
    if minha_cor == 1:
      print(f"\n➤{Fore.MAGENTA}{Style.BRIGHT}Vitória do(a) Jogador(a) {Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}{nome_vez}!!{Style.RESET_ALL}\n⮩Partida encerrada em {jogadas} jogadas")
    else:
       print(f"\n➤{Fore.MAGENTA}{Style.BRIGHT}Vitória do(a) Jogador(a) {Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}{nome_vez}!!{Style.RESET_ALL}\n⮩Partida encerrada em {jogadas} jogadas")
    break

  turno = 1 - turno
