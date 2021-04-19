#Pergunte a quantidade de km percorridas por um carro alugado pelo usuário
#A quantidade de dias pelos quais o carro foi alugado.

#Calcule o preço a pagar
#Sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

distancia = float(input("Escreva a quantidade de km percorridos: "))
tempo = float(input("Escreva a quantidade de dias alugados: "))

preço_km = distancia * 0.15
preço_dias = tempo * 60

preço_total = preço_km + preço_dias

print(f"O preço total a pagar é: {preço_total}")

