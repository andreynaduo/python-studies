# Altere o programa anterior de forma a perguntar também o valor depositado inicialmente. 
# Esse valor será depositado no início de cada mês
# e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito_inicial = float(input("Depósito inicial: "))
deposito_mensal = float(input("Depósito mensal: "))
taxa_juros = float(input("Taxa de juros: "))

total = deposito_inicial
mês = 1

while mês <= 24:
    total = total + taxa_juros + deposito_mensal
    print(f"Mês {mês} = R${total:.2f}")
    mês += 1

print(f"Total: R${total:.2f}")