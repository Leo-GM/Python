###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome:Leonardo Henrique Guimarães 
# RA:247225
###################################################
estoque = 0
n_vendas = 0
lista = []

while True:
    pedidos = int(input())
    if pedidos == 0:
        break
    else:
        lista.append(pedidos)

for pedido in lista:
    
    if pedido < 0:

        if (pedido*(-1)) > estoque:
            print("Quantidade indisponível para a venda de",pedido * (-1) ,"unidades.")
        
        else:
            estoque = estoque + pedido
            n_vendas = n_vendas + 1
    
    if pedido > 0:
        estoque = estoque + pedido

print("Quantidade de vendas realizadas:", n_vendas)
print("Quantidade em estoque:", estoque)
