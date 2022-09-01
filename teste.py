n = 0
OK = True

while OK:
    
    n = int(input(""))

    if n > 0:
        n = n + 1
    else:
        OK = False

print("A quantidade de números inteiros fornecidos é" , n)