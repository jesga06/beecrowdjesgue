renda  = float(input())
imposto = 0
resto1 = 0
resto2 = 0
resto3 = 0
if renda > 4500.00:
    resto1 = renda - 2000
    if resto1 > 1000:
        resto2 = resto1 - 1000
        resto1 -= resto2
        if resto2 > 1500:
            resto3 = resto2 - 1500
            resto2 -= resto3
elif renda >= 3000.01: #até 4500
    resto1 = renda - 2000
    if resto1 > 1000:
        resto2 = resto1 - 1000
        resto1 -= resto2
        if resto2 > 1500:
            resto3 = resto2 - 1500
            resto2 -= resto3
elif renda >= 2000.01: #até 3000
    resto1 = renda - 2000
    if resto1 > 1000:
        resto2 = resto1 - 1000
        resto1 -= resto2
if resto1 > 0:
    imposto = resto1 * 0.08
if resto2 > 0:
    imposto = (resto1 * 0.08) + (resto2 * 0.18)
if resto3 > 0:
    imposto = (resto1 * 0.08) + (resto2 * 0.18) + (resto3 * 0.28)
if imposto != 0:
    print(f"R$ {imposto:.2f}")
else:
    print("Isento")