cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? R:"))
anos_fumando = int(input("Há quantos anos você fuma? R:"))

dias_fumando = anos_fumando * 365
total_cigarros = dias_fumando * cigarros_por_dia

minutos_perdidos = total_cigarros * 10
horas_perdidas = minutos_perdidos / 60
dias_perdidos = horas_perdidas / 24

print(f"Você perderá {dias_perdidos:.0f} dias de vida.")
print("Pare de fumar, cigarro dá câncer, diga não às drogas.")
