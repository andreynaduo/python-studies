#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, de 15%.

salario = float(input("Informe o valor do salário: "))

if salario > 1.250:
    aumento1 = 10 * salario / 100
    salario = salario + aumento1
    print(f"O valor do aumento é R${aumento1:.2f}")
    print(f"Portanto o novo valor do salário é R${salario:.2f}")
elif salario <= 1.250: 
    aumento2 = 15 * salario / 100
    salario = salario + aumento2
    print(f"O valor do aumento é R${aumento2:.2f}")
    print(f"Portanto o novo valor do salário é R${salario:.2f}")

# Não sei o que acontece que parece que no elif ele não multiplica o valor por 15
# Então o resultado aparece como se fosse 10%
# Tentei achar o problema mas não consegui :(