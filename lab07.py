defensores = []
atacantes = []
resultados = []


n1 = int(input())
for i in range(n1):
    defesa = int(input())
    defensores.append(defesa)

n2 = int(input())
for i in range(n2):
    ataque = int(input())
    atacantes.append(ataque)


if len(atacantes) > len(defensores):
    nPartidas = len(defensores)
    nMenor = len(atacantes)
else:
    nPartidas = len(atacantes)
    nMenor = len(defensores)


for defensor in range(nMenor - nPartidas + 1): 
    nEmpates = 0
    nVitorias = 0
    for atacante in range(len(atacantes)):
        
        if atacantes[atacante] > defensores[defensor + atacante]:
            nVitorias = nVitorias + 1
            
        elif atacantes[atacante] == defensores[defensor+atacante]:
            nEmpates = nEmpates + 1
        
    if nVitorias > ((nPartidas - nEmpates) / 2):
        print("Vitória posicionando as tropas a partir da posição {}".format(defensor + 1))
        exit()

print("Derrota")