#Modifique o programa anterior de forma que 
# o usuário também digite o início e fim da tabuada, em vez de começar com 1 e 10.

n = int(input("Tabuada de:"))
x = int(input("Início da tabuada: "))
fim = int(input("Fim da tabuada: "))

while x <= fim:
    tabuada = n * x
    print(f"{n}x{x}={tabuada}")
    x = x + 1
