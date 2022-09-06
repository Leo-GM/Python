a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("O triângulo é equilátero")
elif (a == b != c) or (a == c != b) or (a != b == c):
    print("O triângulo é isósceles")

elif a != b != c:
    print("O triângulo é escaleno")