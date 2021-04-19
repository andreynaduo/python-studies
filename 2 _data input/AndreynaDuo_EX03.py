dias = int(input("Escreva a quantidade de dias: "))
horas = float(input("Escreva a quantidade de horas: "))
minutos = float(input("Escreva a quantidade de minutos: "))

#1 - Transformar dias em horas
#2 - Transfomrar horas em minutos
#3 - Transformar minutos em segundos

dias_em_horas = dias * 24
horas_em_minutos = (dias_em_horas + horas) * 60
minutos_em_segundos = horas_em_minutos * 60

print(f"O total em segundos é {minutos_em_segundos}")

