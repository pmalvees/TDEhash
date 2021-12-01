K = 10
TAMANHO = 2 ** K
WORD = 64
A = 9

tabela = [None for i in range(TAMANHO)]

def posicao(chave):
  e = chave * (A / WORD)
  e = e % TAMANHO
  return e

def insere(valor):
  pos = posicao(valor)
  tabela[pos] = valor