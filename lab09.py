###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Leonardo Henrique Guimarães
# RA: 247225
###################################################

estoque = {}

while True:
    a = input()
    
    if a == "FIM":
        break

    nome, pedido = a.split(" : ")
    pedido = int(pedido)

    if pedido > 0:

        if nome in estoque:
            estoque[nome] = [estoque[nome][0] + pedido, estoque[nome][1] + 1, estoque[nome][2]]
        
        else:
            estoque[nome] = [pedido , 1 , 0]
    
    else:

        if nome in estoque:

                if estoque[nome][0] + pedido >= 0:
                    estoque[nome] = [estoque[nome][0] + pedido,estoque[nome][1] , estoque[nome][2] + 1]
                
                else:
                    print("Quantidade indisponivel para a venda de {} unidade(s) do produto {}.". format(pedido*-1, nome))
        else:
            print("Quantidade indisponivel para a venda de {} unidade(s) do produto {}.". format(pedido*-1, nome))

ordenado = sorted(estoque)

for i in ordenado:
    print("Produto: {}".format(i))
    print("Quantidade em Estoque: {}".format(estoque[i][0]))    
    print("Pedidos de Compra: {}".format(estoque[i][1]))
    print("Pedidos de Venda: {}".format(estoque[i][2]))