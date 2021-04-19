#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela.

faixa = float(input("Informe a quantidade de kWh consumida: "))
tipo = input("Informe o tipo de instalação: ")

if tipo == "R":
    if faixa <= 500:
        print("O preço a pagar é R$ 0,40")
    else:
        print("O preço a pagar é R$ 0,65")
elif tipo == "C":
    if faixa <= 1000:
        print("O preço a pagar é R$ 0,55")
    else:
        print("O preço a pagar é R$ 0,60")
elif tipo =="I":
    if faixa <= 5000:
        print("O preço a pagar é R$ 0,55")
    else:
        print("O preço a pagar é R$ 0,6")



