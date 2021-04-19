#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada.

a = float(input("1º número: "))
operação = input("Qual operação você deseja fazer? (+) (-) (x) (%): ")
b = float(input("2º número: "))

if operação == "+":
    soma = a + b
    print(f"Resultado: {soma}")
elif operação == "-": 
    subtração = a - b
    print(f"Resultado: {subtração}")
elif operação == "x":
    multiplicação = a * b
    print(f"Resultado: {multiplicação}")
elif operação == "%":
    divisão = a / b
    print(f"Resultado: {divisão}")
else:
    print("Não foi possível realizar a operação pois você não digitou um símbolo válido.")
