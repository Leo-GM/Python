##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome:Leonardo Henrique Guimarães  
# RA:247225
##################################################



valor = int(input())
dias = int(input())
horas = 0
extra = 0

for dia in range(1, (dias + 1)):
    
    periodos = int(input())
    horasDia = 0
    for periodo in range(1, (periodos + 1)):
        
        inicio = int(input())
        fim = int(input())
            
        horasDia = horasDia + (fim - inicio)

    if horasDia > 8:
        extra = extra + (horasDia - 8)
        horas = horas + 8
    else:
        horas = horas + horasDia

if horas > 44:
    extra = extra + horas - 44
    horas = 44
           
ganhos = (valor * horas) + (extra * 1.5 * valor)

print("Horas trabalhadas: {}".format(horas + extra))
print("Horas extras: {}".format(extra))
print("Valor devido: R$ {:0.2f}".format(ganhos))
