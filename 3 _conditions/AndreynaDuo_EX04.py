# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$
# 0,45 para viagens mais longas.

distancia = float(input("Informe a distância que deseja percorrer: "))

if distancia <= 200:
    preço_passagem = distancia*0.50
    print(f"O preço da passagem é R${preço_passagem:.2f}")
else:
    preço_passagem = distancia*0.45
    print(f"O preço da passagem é R${preço_passagem:.2f}")
