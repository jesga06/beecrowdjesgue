n = int(input())
no = n
n100 = n // 100
n -= n100 * 100
n50 = n // 50
n -= n50 * 50
n20 = n // 20
n -= n20 * 20
n10 = n // 10
n -= n10 * 10
n5 = n // 5
n -= n5 * 5
n2 = n // 2
n -= n2 * 2
n1 = n // 1
print(no)
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")