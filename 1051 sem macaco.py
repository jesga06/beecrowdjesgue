renda = float(input())
imposto = 0
if renda > 4500:
    imposto += (renda - 4500) * 0.28
    renda = 4500
if renda > 3000:
    imposto += (renda - 3000) * .18
    renda = 3000
if renda > 2000:
    imposto += (renda - 2000) * 0.08
    renda = 2000
print(imposto)