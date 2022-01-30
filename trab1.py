import random

class tabuleiro:
  def __init__(self, N_queens) :
    self.tabuleiro = []
    self.tabuleiro.append([1 for x in range(N_queens)])
    for i in range(N_queens-1):
      self.tabuleiro.append([0 for x in range(N_queens)])

  def numAttacks(self, tabuleiro):
    attacks = 0
    for linha in range(len(tabuleiro)):
      for coluna in range(len(tabuleiro)):
        if(tabuleiro[linha][coluna] == 1):
          for i in range(len(tabuleiro)):
            if(tabuleiro[linha][i] == 1 and coluna != i):
              attacks = attacks + 1
            if(tabuleiro[i][coluna] == 1 and linha != i):
              attacks = attacks + 1
          
          if(coluna < linha):
            diagonal = linha
          else:
            diagonal = coluna
          for i in range(diagonal,(len(tabuleiro)-diagonal)):
            if(tabuleiro[linha + i][coluna + i] == 1 and i != 0):
              attacks += 2
          
          if(not(coluna == 0 or linha == len(tabuleiro)-1)):
            if(coluna > linha):
              diagonal = linha
            else:
              diagonal = coluna

          i = 1
          while (linha + i < len(tabuleiro) and coluna - i < 0 ):
            print(linha, coluna, tabuleiro)
            if(tabuleiro[linha + i][coluna - i] == 1):          
              attacks += 2
            i += 1
    return attacks 

  def buscaEmProfundidadeIterativa(self,deth, maxDeth, atual) :
    if(deth == maxDeth):
      if(self.numAttacks(atual) == 0):
        print(atual)
        return atual
      return 0
    else:
      deth = deth + 1
    tabuleiroTemporario = []
    tabuleiroTemporario = self.copiaLista(atual)
    
    for linha in range(len(atual)):
      # Inicio do movimento da peça 
      for i in range(len(atual)):
        if(tabuleiroTemporario[i][deth] == 1):
          tabuleiroTemporario[i][deth] = 0
          break
      tabuleiroTemporario[linha][deth] = 1
      # Fim do movimento da peça
      
      if(self.buscaEmProfundidadeIterativa(deth, maxDeth, tabuleiroTemporario)):
        return tabuleiroTemporario
      tabuleiroTemporario = []
      tabuleiroTemporario = self.copiaLista(atual)

  def hillClibing(self, atual):

    opcoes = []
    opcoes.append(self.copiaLista(atual))
    tabuleiroTemporario = []
    tabuleiroTemporario = self.copiaLista(atual)

    for coluna in range(len(atual)):
        for linha in range(len(atual)):
          # Inicio do movimento da peça 
          for i in range(len(atual)):
            if(tabuleiroTemporario[i][coluna] == 1):
              tabuleiroTemporario[i][coluna] = 0
              break
          tabuleiroTemporario[linha][coluna] = 1
          # Fim do movimento da peça
          opcoes.append(self.copiaLista(tabuleiroTemporario))
          tabuleiroTemporario = []
          tabuleiroTemporario = self.copiaLista(atual)
          
    min = len(self.tabuleiro)*10
    tabuleiroMinimo = 0
    for i in opcoes:
      x = self.numAttacks(i)
      if(x < min):
        min = x
        tabuleiroMinimo = i
    if( min == 0 ):
      print(tabuleiroMinimo)
      return tabuleiroMinimo
    else:
      return self.hillClibing(tabuleiroMinimo)

  def simulatedAnnealing(self, temperatura, atual):
    valorInicial = self.numAttacks(atual)
    if(valorInicial == 0):
      print(atual)
      return atual
    tabuleiroTemporario = []
    tabuleiroTemporario = self.copiaLista(atual)
    for coluna in range(len(atual)):
        for linha in range(len(atual)):

          # Inicio do movimento da peça 
          for i in range(len(atual)):
            if(tabuleiroTemporario[i][coluna] == 1):
              tabuleiroTemporario[i][coluna] = 0
              break
          tabuleiroTemporario[linha][coluna] = 1
          # Fim do movimento da peça

          valorAtual = self.numAttacks(tabuleiroTemporario)
          deltaE = (valorAtual - valorInicial) * (-1)
          if(deltaE > 0):
            return self.simulatedAnnealing(temperatura-0.3, tabuleiroTemporario)
          else:
            if (2.7182**(deltaE/temperatura) < random.random()):
              return self.simulatedAnnealing(temperatura-0.3, tabuleiroTemporario)
          tabuleiroTemporario = []
          tabuleiroTemporario = self.copiaLista(atual)

  def copiaLista(self, listaOriginal):
    listaCopia = []
    linha = []
    for i in listaOriginal:
      for j in i:
        linha.append(j)
      listaCopia.append(linha)
      linha = []
    return listaCopia

class __main__:
  numberOfQueens = int(input("Quantidade de rainhas que serão inseridas: "))
  jogo =  tabuleiro(numberOfQueens)
  # for i in range(0, len(jogo.tabuleiro)):
  #   jogo.buscaEmProfundidadeIterativa(0, i, jogo.tabuleiro)
  jogo.hillClibing(jogo.tabuleiro)
  # jogo.simulatedAnnealing(2, jogo.tabuleiro)