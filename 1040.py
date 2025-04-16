n1, n2, n3, n4 = (input()).strip().split()
mp = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) /  10
print(f"Media: {float(mp)}")
if mp >= 7.0:
    print("Aluno aprovado.")
elif mp < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nf = float(input())
    print(f"Nota do exame: {nf}")
    nftrue = (mp + nf) / 2
    if nftrue >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {nftrue}")