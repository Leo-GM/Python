dia = int(input())
hora = int(input())
minuto = int(input())
estudante = input()
pagamento = input()

tempo = (hora * 60) + 30

if dia == 1:
   
    valor = 30

    if estudante == "N":
        if pagamento == "D":
            valor = valor
        else:   
            valor = valor * (7/10)
    
    else:
        valor = valor * (1/2)

if tempo <= 1110:
        
    if (dia == 2) or (dia == 3) or (dia == 4):
        valor = 15
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)

    elif (dia == 5) or (dia == 6):
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
                valor = valor * (8/10)
        else:
            valor = valor * (1/2)

if tempo > 1110:
    
    if (dia == 2) or (dia == 3):
        valor = 20
        if estudante == "N":
            if pagamento == "D":
                valor = valor
            else:
                valor = valor * (1/2)
        else:
            valor = valor * (1/2)

    elif (dia == 4) or (dia == 5):
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
                valor = valor * (8/10)
        else:
            valor = valor * (1/2)

print('Valor do ingresso: R$', format(valor, '.2f').replace('.', ','))
