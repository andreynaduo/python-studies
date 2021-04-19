# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período.

deposito_inicial = float(input("Depósito inicial: "))
taxa_juros = float(input("Taxa de juros: "))

total = deposito_inicial
x = 1

while x <= 24:
    total += taxa_juros
    print(f"Mês {x} = R${total:.2f}")
    x += 1

print(f"Total: R${total:.2f}")
    
