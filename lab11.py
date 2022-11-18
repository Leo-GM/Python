peca90g = []
peca180g = []
peca270g = []
# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for a in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca0g = []
for b in range(P):
  peca0g.append(input().split())

def rotacionaPeca(x, y):
  tamI = int(len(x))
  tamJ = int(len(x[0]))
  for i in range(tamJ):
    if len(y) <= i:
      y.append([])
    for j in range(tamI):
      y[i].append(x[((tamI-1)-j)][(i)])

rotacionaPeca(peca0g, peca90g)
rotacionaPeca(peca90g, peca180g)
rotacionaPeca(peca180g, peca270g)



def TxP(peca):
  tamIT = int(len(tabuleiro))
  tamJT = int(len(tabuleiro[0]))
  tamIP = int(len(peca))
  tamJP = int(len(peca[0]))

  movX = (tamJT - tamJP)
  movY = (tamIT - tamIP)
  n = 0

  for y in range(movY + 1):
    temp = 0
    for x in range(movX + 1 ):
      temp = 0
      control = False
      for i in range(tamIP):
        for j in range(tamJP):
          if (tabuleiro[y+i][x+j] == "X") and (peca[i][j] == "X"):
            control = True
            break
        if control:
          break
      if not control:
        n += 1
  return n

  

a = TxP(peca0g)
b = TxP(peca90g)
c = TxP(peca180g)
d = TxP(peca270g)
print("{},{},{},{}".format(a, b, c, d))