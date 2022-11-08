n = int(input())
matriz = [input().split() for i in range(n)]

primeiro = input()
nJogadores = int(input())
vermelho = nJogadores / 2
azul = vermelho
tesouroA = 0
tesouroV = 0

for i in range(1, nJogadores + 1):
    
   
    posX = 0
    posY = 0
    posX2 = 0
    posY2 = 0

    if i % 2 == 1:
        posicionamentoV = ""
        posicionamentoA = ""


        if primeiro == "vermelho":
            if i % 2 == 1:
                posicionamentoV = input()
                posicionamentoA = input()
                listaPV = list(posicionamentoV)
                listaPA = list(posicionamentoA)
        else:
            if i % 2 == 1:
                posicionamentoA = input()
                posicionamentoV = input()
                listaPA = list(posicionamentoA)
                listaPV = list(posicionamentoV)
            
    
    for caminho in range(50):
        if primeiro == "vermelho":
            if i % 2 == 1:
                try:
                    if listaPV[caminho] == "N":
                        posY += -1
                        if matriz[posY][posX] == "*":
                            tesouroV += 1
                            matriz[posY][posX] = "."
                    if listaPV[caminho] == "S":
                        posY += 1
                        if matriz[posY][posX] == "*":
                            tesouroV += 1
                            matriz[posY][posX] = "."
                    if listaPV[caminho] == "L":
                        posX += 1
                        if matriz[posY][posX] == "*":
                            tesouroV += 1
                            matriz[posY][posX] = "."
                    if listaPV[caminho] == "O":
                        posX += -1   
                        if matriz[posY][posX] == "*":
                            tesouroV += 1 
                            matriz[posY][posX] = "."
                except IndexError:
                    continue
            else:
                try:
                    if listaPA[caminho] == "N":
                        posY += -1
                        if matriz[posY][posX] == "*":
                            tesouroA += 1
                            matriz[posY][posX] = "."
                    if listaPA[caminho] == "S":
                        posY += 1
                        if matriz[posY][posX] == "*":
                            tesouroA += 1
                            matriz[posY][posX] = "."
                    if listaPA[caminho] == "L":
                        posX += 1
                        if matriz[posY][posX] == "*":
                            tesouroA += 1
                            matriz[posY][posX] = "."
                    if listaPA[caminho] == "O":
                        posX += -1
                        if matriz[posY][posX] == "*":
                            tesouroA += 1
                            matriz[posY][posX] = "."
                except IndexError:
                    continue
        else:
            if i % 2 == 1: 
                try:
                    if listaPA[caminho] == "N":
                        posY2 += -1
                        if matriz[posY2][posX2] == "*":
                            tesouroA += 1
                            matriz[posY2][posX2] = "."
                    if listaPA[caminho] == "S":
                        posY2 += 1
                        if matriz[posY2][posX2] == "*":
                            tesouroA += 1
                            matriz[posY2][posX2] = "."
                    if listaPA[caminho] == "L":
                        posX2 += 1
                        if matriz[posY2][posX2] == "*":
                            tesouroA += 1
                            matriz[posY2][posX2] = "."
                    if listaPA[caminho] == "O":
                        posX2 += -1
                        if matriz[posY2][posX2] == "*":
                            tesouroA += 1
                            matriz[posY2][posX2] = "."
                except IndexError:
                    continue
            else:
                try:
                    if listaPV[caminho] == "N":
                        posY2 += -1
                        if matriz[posY2][posX2] == "*":
                            tesouroV += 1
                            matriz[posY2][posX2] = "."
                    if listaPV[caminho] == "S":
                        posY2 += 1
                        if matriz[posY2][posX2] == "*":
                            tesouroV += 1
                            matriz[posY2][posX2] = "."
                    if listaPV[caminho] == "L":
                        posX2 += 1
                        if matriz[posY2][posX2] == "*":
                            tesouroV += 1
                            matriz[posY2][posX2] = "."
                    if listaPV[caminho] == "O":
                        posX2 += -1
                        if matriz[posY2][posX2] == "*":
                            tesouroV += 1
                            matriz[posY2][posX2] = "."
                except IndexError:
                    continue

print("Tesouros encontrados pelo time azul: {}".format(tesouroA))
print("Tesouros encontrados pelo time vermelho: {}".format(tesouroV))

if tesouroA == tesouroV:
    print("Empate")
elif tesouroA > tesouroV:
    print("Vitoria do time azul")
else:
    print("Vitoria do time vermelho")
