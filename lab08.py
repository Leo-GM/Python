###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Leonardo Henrique Guimarães
# RA: 247225
###################################################
import sys
resposta = input()
lista1 = list(resposta)
saida = ""
for i in range(1,7):
    try:
        chute = input()
        lista2 = list(chute)
        if chute == resposta:
            print(resposta.upper()+"\nResposta correta")
            sys.exit()
        saida = ""
        for letra in range(0,len(chute)):
            if lista1[letra] == lista2[letra]:
                saida = saida + lista1[letra].upper()
            elif lista2[letra] in lista1:
                saida = saida + lista2[letra]
            else:
                saida = saida + "_"
        a = "".join(map(str, saida))
        print(a)
    except EOFError:
        break
print("Palavra correta: {}".format(resposta))
