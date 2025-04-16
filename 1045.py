lados = input().strip().split()
lados.sort(reverse=True)
a = float(lados[0])
b = float(lados[1])
c = float(lados[2])
if a >= b+c:
    print("NAO FORMA TRIANGULO")
if a ** 2 == (b ** 2) + (c ** 2):
    print("TRIANGULO RETANGULO")
if a ** 2 < (b ** 2) + (c ** 2):
    print("TRIANGULO ACUTANGULO")
if a ** 2 > (b ** 2) + (c ** 2):
    print("TRIANGULO OBTUSANGULO")
if a == b and a == c and b == c:
    print("TRIANGULO EQUILATERO")
if a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")