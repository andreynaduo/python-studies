#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe o salário: R$"))
anos_a_pagar = int(input("Informe a quantidade de anos a pagar: "))

meses_a_pagar = anos_a_pagar * 12
prestação = valor_casa / meses_a_pagar
porcentagem_salario = 30 * salario / 100

if prestação > porcentagem_salario:
    print("Não aprovado")
else:
    print("Aprovado")
    print(f"O valor da prestação é R${prestação}")
