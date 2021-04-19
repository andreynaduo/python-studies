valor_do_produto = float(input("Insira o valor do produto: "))
desconto = float(input("Insira o percentual do desconto: "))

desconto = valor_do_produto * desconto/100
valor_do_produto = valor_do_produto - desconto

print(f"O valor do desconto é: R${desconto:<10.2f}")
print(f"O preço a pagar é: R${valor_do_produto:<10.2f}")
