# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
# Pergunte também o valor mensal que será pago. 
# Imprima o maior número de meses para que a dívida seja paga, o total pago e o total de juros pago.

valor_inicial = float(input("Valor inicial da dívida: "))
juro_mensal = float(input("Juro mensal: "))
pagamento_mensal = float(input("Valor mensal que será pago: "))

total_pagamento = pagamento_mensal
total_juros = juro_mensal 
meses = 1

while total_pagamento <= valor_inicial:
    total_pagamento += pagamento_mensal
    total_juros += juro_mensal
    meses += 1
print(f"A dívida será paga em {meses} meses \nTotal pago: R${total_pagamento:.2f} \nTotal de juros: R${total_juros:.2f}")
    

