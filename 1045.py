lados = input().strip().split()
lados.sort(reverse=True)
a = float(lados[0])
b = float(lados[1])
c = float(lados[2])
if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")
    elif a ** 2 < (b ** 2) + (c ** 2):
        print("TRIANGULO ACUTANGULO")
    elif a ** 2 > (b ** 2) + (c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if a == b and a == c and b == c:
        print("TRIANGULO EQUILATERO")
    if a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")

"""código q funciona de acordo com o gpt
# Leitura e ordenação
lados = list(map(float, input().split()))
lados.sort(reverse=True)
a, b, c = lados

# Caso não forme triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # Tipos de ângulo
    if a*a == b*b + c*c:
        print("TRIANGULO RETANGULO")
    elif a*a > b*b + c*c:
        print("TRIANGULO OBTUSANGULO")
    else:  # a*a < b*b + c*c
        print("TRIANGULO ACUTANGULO")
    
    # Tipos de lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")"""