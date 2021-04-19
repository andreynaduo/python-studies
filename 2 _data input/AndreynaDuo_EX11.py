
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

maiorAB = (a+b+abs(a-b))/2

maiorABC = (maiorAB+c+abs(maiorAB-c))/2

print(f"{maiorABC:.0f} eh o maior")
