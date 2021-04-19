# Escreva um programa que leia dois números. 
# Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
# Assim,
# 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

numero1 = int(input("Insira o 1º número: "))
numero2 = int(input("Insira o 2º número: "))
n = 1
conta = 0

while n <= numero2:
    conta += numero1
    n += 1
print(f"Resultado: {conta}")

