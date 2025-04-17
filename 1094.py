experimentos = int(input())
totalcobaia = 0
typecobaia = 0
ratos = 0
coelhos = 0
sapos = 0
pcoelhos = 0
pratos = 0
psapos = 0
for y in range(0, experimentos):
    usedcobaia = input()
    numcobaia = (usedcobaia.split()[0])
    totalcobaia += int(numcobaia)
    typecobaia = (usedcobaia.split()[1])
    if typecobaia == "C":
        coelhos += int(numcobaia)
    elif typecobaia == "R":
        ratos += int(numcobaia)
    elif typecobaia == "S":
        sapos += int(numcobaia)
pcoelhos = ((coelhos / totalcobaia) * 100)
pratos = ((ratos / totalcobaia) * 100)
psapos = ((sapos / totalcobaia) * 100)
print(f"Total: {totalcobaia} cobaias\nTotal de coelhos: {coelhos}\nTotal de ratos: {ratos}\nTotal de sapos: {sapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f} %")
print(f"Percentual de ratos: {pratos:.2f} %")
print(f"Percentual de sapos: {psapos:.2f} %")