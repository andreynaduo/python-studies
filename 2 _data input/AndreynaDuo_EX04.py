salario = float(input("Digite o valor do salário: "))
aumento = float(input("Digite a porcentagem do aumento: "))

aumento = salario * aumento/100
salario = salario + aumento
print(f"O valor do aumento é: R${aumento:<10.2f}")
print(f"O valor do novo salário é: R${salario:<10.2f}")
