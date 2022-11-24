def imprimir_imagem(imagem):
    n2 = (2 * n - 1)
    m2 = (2 * m - 1)
    print("P2")
    print(m2, n2)
    print("255")
    for i in range(n2):
        print(" ".join(str(int(x)) for x in imagem[i]))
        
def expansao(imagem_original):
    n2 = (2 * n - 1)
    m2 = (2 * m - 1)
    imagemB = [[0 for j in range(m2)] for i in range(n2)]

    #step 1
    try:
        for i in range(1, n+1):
            for j in range(1, m+1):
                i2 = i*2 - 1
                j2 = j*2 - 1
                imagemB[i2-1][j2-1] = imagem_original[i-1][j-1]

    except IndexError:
        print("erro1")
        a = 0
    
    try:
        for i in range(1, n2 + 1):
            for j in range(1, m2 + 1):
                if ((i % 2 == 1) and (j % 2 == 0)):
                    imagemB[i - 1][j - 1] = (int(((imagemB[i - 1][j - 2]) + (imagemB[i - 1][j])) / 2))
    except IndexError:
        print("erro2")
        a = 0    
    
    try:
        for i in range(1, n2 + 1):
            for j in range(1, m2 + 1):
                if ((i % 2 == 0) and (j % 2 == 1)):
                    imagemB[i - 1][j - 1] = (int(((imagemB[i - 2][j - 1]) + (imagemB[i][j - 1])) / 2))
    except IndexError:
        print("erro3")
        a = 1
    
    try:
        for i in range(1, n2 + 1):
            for j in range(1, m2 + 1):
                if ((i % 2 == 0) and (j % 2 == 0)):
                    imagemB[i - 1][j - 1] = (int(((imagemB[i - 2][j - 2]) + (imagemB[i - 2][j]) + (imagemB[i][j - 2]) + (imagemB[i][j])) / 4))
        #print(imagemB)
    except IndexError:
        print("erro4")
        a = 1
    print("P2")
    print(m2, n2)
    print("255")
    for i in range(n2):
        print(" ".join(str(int(x)) for x in imagemB[i]))


def retracao(imagem_original):
    if n % 2 == 0:
        n2 = n // 2
    else:
        n2 = (n + 1) // 2
    if m % 2 == 0:
        m2 = m // 2
    else:
        m2 = (m + 1) // 2
    imagemB = [[0 for j in range(m2)] for i in range(n2)]
    try:
        for i in range(1, n + 1, 2):
            for j in range(1, m + 1, 2):
                i2 = i // 2
                j2 = j // 2
                if (i == n) and (j == m):
                    media = imagem_original[i - 1][j - 1]
                    imagemB[i2][j2] = media
                    break
                if (i == n) and (j != m):
                    media = (imagem_original[i - 1][j - 1] + imagem_original[i - 1][j]) / 2
                    imagemB[i2][j2] = media
                    continue
                if (i != n) and (j == m):
                    media = (imagem_original[i - 1][j - 1] + imagem_original[i][j - 1]) / 2
                    imagemB[i2][j2] = media
                    continue
                else:
                    media = (imagem_original[i][j] + imagem_original[i - 1][j - 1] + imagem_original[i - 1][j] + imagem_original[i][j - 1]) / 4
                    imagemB[i2][j2] = media
                    

    except IndexError:
        print("erro")
        a = 0
    print("P2")
    print(m2, n2)
    print("255")
    for i in range(n2):
        print(" ".join(str(int(x)) for x in imagemB[i]))



    
# leitura da imagem
tipo_imagem = input() #P2

m, n = [int(x) for x in input().split()]

linha_ignorada = input() #255
imagemB = []
imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# escolha do redimensionamento
tipo_redimensionamento = input()
if tipo_redimensionamento == "retracao":
    retracao(imagem_original)
else:
    expansao(imagem_original)

