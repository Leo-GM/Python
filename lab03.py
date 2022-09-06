###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome:Leonardo Henrique Guimarães
# RA:247225
###################################################

dia = int(input())
hora = int(input())
minuto = int(input())
estudante = input()
pagamento = input()

if dia == 1:
   
    valor = 30

    if estudante == "N":
        if pagamento == "D":
            valor = valor
        else:
            valor = valor * (7/10)
    
    elif estudante == "S":
        valor = valor * (1/2)

## HORÁRIO 18:30 +++###
if (hora >= 18) and (minuto >= 30):
    if dia == 2:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 3:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 4:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 5:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 6:
        valor = 40
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (7/10)
        else:
            valor = valor * (1/2)
    elif dia == 7:
        valor = 40
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (2/10)
        else:
            valor = valor * (1/2)

## HORÁRIO 18:30++++##

elif (hora > 18):
    if dia == 2:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 3:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 4:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 5:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 6:
        valor = 40
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (7/10)
        else:
            valor = valor * (1/2)
    elif dia == 7:
        valor = 40
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (2/10)
        else:
            valor = valor * (1/2)
##HORÁRIO 18:30 ---##
elif (hora >= 18) and (minuto < 30):
    if dia == 2:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 3:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 4:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 5:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 6:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 7:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (2/10)
        else:
            valor = valor * (1/2)
##HORÁRIO 18:30 ---##
elif (hora < 18):
    if dia == 2:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 3:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 4:
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 5:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 6:
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)
    elif dia == 7:
        valor = 30
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (2/10)
        else:
            valor = valor * (1/2)
    

print('Valor do ingresso: R$', format(valor, '.2f').replace('.', ','))
