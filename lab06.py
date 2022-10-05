##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:Leonardo Henrique Guimarães 
# RA:247225
##################################################

panquecas = [int(i) for i in input().split()]

while True:
    m = int(input())

    if m == 0:
        break
    else:
       panquecas = panquecas[m-1::-1] + panquecas[m:]

if panquecas == sorted(panquecas):
    print("Torre estavel")
else:
    print("Torre instavel")
