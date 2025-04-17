dia1 = input()
horario1 = input()
dia1 = int(dia1.split()[1])
hr1 = int(horario1.split()[0])
min1 = int(horario1.split()[2])
sec1 = int(horario1.split()[4])
dia2 = input()
horario2 = input()
dia2 = int(dia2.split()[1])
hr2 = int(horario2.split()[0])
min2 = int(horario2.split()[2])
sec2 = int(horario2.split()[4])
#duracao
segundos1 = sec1 + (min1 * 60) + (hr1 * 3600) + (dia1 * 24 * 3600)
segundos2 = sec2 + (min2 * 60) + (hr2 * 3600) + (dia2 * 24 * 3600)
difsec = segundos2 - segundos1
dias = difsec // (24 * 3600)
difsec %= (24 * 3600)
horas = difsec // 3600
difsec %= 3600
minutos = difsec // 60
segundos = difsec % 60
#segundos = (sec2 + sec1) + ((min2 - min1) * 60) + (((hr2 - hr1) * 60) * 60) + ((((dia2 - dia1) * 24) * 60) * 60) - 46
#minutos = int(segundos / 60)
#horas = int(minutos // 60)
#dias = int(horas // 24)
print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
