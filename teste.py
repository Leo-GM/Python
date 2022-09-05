###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome:Leonardo Henrique Guimarães
# RA:247225
###################################################


dia_da_semana = int(input())
hora_de_início = int(input())
minuto_de_início = int(input())
estudante = input()
pagamento = input()

if dia_da_semana > 7:
    print("Erro")

elif hora_de_início > 23:
    print("Erro")

elif minuto_de_início > 60:
    print("Erro")

elif (estudante != 'S') and (estudante != 'N'):
    print("Erro")

elif (pagamento != 'D') and (pagamento != 'C'):
    print("Erro")

if dia_da_semana == 1:
   
    valor = 30

    if estudante == "N":
        if pagamento == "D":
            valor = valor
        else:
            valor = valor * (7/10)
    
    elif estudante == "S":
        valor = valor * (1/2)

if dia_da_semana == 2:
   
    if hora_de_início >= 18:
        if (minuto_de_início >= 30) or (hora_de_início >= 19):
            valor = 20
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
        elif minuto_de_início < 30:
            valor = 15
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 15
        if (estudante == "S") or (pagamento == "C"):
            valor = valor * (1/2)
            if (estudante == "N") or (pagamento == "D"):
                valor = valor

if dia_da_semana == 3:
   
    if hora_de_início >= 18:
        if (minuto_de_início >= 30) or (hora_de_início >= 19):
            valor = 20
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
        if minuto_de_início < 30:
            valor = 15
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 15
        if (estudante == "S") or (pagamento == "C"):
            valor = valor * (1/2)
            if (estudante == "N") or (pagamento == "D"):
                valor = valor

if dia_da_semana == 4:
   
    if hora_de_início >= 18:
        if (minuto_de_início >= 30) or (hora_de_início >= 19):
            valor = 30
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
        if minuto_de_início < 30:
            valor = 15
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 15
        if (estudante == "S") or (pagamento == "C"):
            valor = valor * (1/2)
            if (estudante == "N") or (pagamento == "D"):
                valor = valor

if dia_da_semana == 5:
   
    if (minuto_de_início >= 30) or (hora_de_início >= 19):
        if minuto_de_início >= 30:
            valor = 30
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
        if minuto_de_início < 30:
            valor = 20
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 20
        if (estudante == "S") or (pagamento == "C"):
            valor = valor * (1/2)
            if (estudante == "N") or (pagamento == "D"):
                valor = valor

if dia_da_semana == 6:
   
    if hora_de_início >= 18:
        if (minuto_de_início >= 30) or (hora_de_início >= 19):
            valor = 40
            if pagamento == "C":
                valor = valor * (7/10)
                if estudante == "S":
                    valor = valor * (1/2)
                    if (estudante == "N") or (pagamento == "D"):
                        valor = valor
        if minuto_de_início < 30:
            valor = 20
            if (estudante == "S") or (pagamento == "C"):
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 20
        if (estudante == "S") or (pagamento == "C"):
            valor = valor * (1/2)
            if (estudante == "N") or (pagamento == "D"):
                valor = valor

if dia_da_semana == 7:
   
    if hora_de_início >= 18:
        if minuto_de_início >= 30:
            valor = 40
            if pagamento == "C":
                valor = valor * (8/10)
                if estudante == "S":
                    valor = valor * (1/2)
                    if (estudante == "N") or (pagamento == "D"):
                        valor = valor
        if minuto_de_início < 30:
            valor = 30
            if pagamento == "C":
                valor = valor * (8/10)
                if estudante =="S":
                    valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor
    else:
        valor = 30
        if pagamento == "C":
            valor = valor * (8/10)
            if estudante == "S":
                valor = valor * (1/2)
                if (estudante == "N") or (pagamento == "D"):
                    valor = valor

print('Valor do ingresso: R$', format(valor, '.2f').replace('.', ','))





    


