total_segundos = int(input("Informe o valor: "))

segundos = total_segundos % 60
minutos = total_segundos / 60
horas = total_segundos / 3600

print(f"{horas:02.0f}:{minutos:02.0f}:{segundos:02.0f}")

#Infelizmente não consegui fazer exatamente o que o enunciado tinha pedido
#O mais próximo que consegui chegar foi isso

