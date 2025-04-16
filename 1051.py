renda = float(input()).__round__(2)
if renda <= 2000.00:
    print("Isento")
elif renda > 2000.00:
    imposto = (renda - 2000.00) * 1.08
    print(f"R$ {imposto}")
