###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome:Leonardo Henrique Guimarães
# RA:247225
###################################################

D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())

##SpaceX
t1 = (D1 / V1) / 24
##Blue Origin
t2 = (D2 / V2) / 24


if t1 < T:
    print("True")

elif t1 > t2 + T:
    print("False")

elif t1  < t2 + T:
    print("True")
