#Altere o programa dado em aula para exibir os resultados no mesmo formato de uma tabuada:
#2 × 1 = 2, 2 × 2 = 4, . . .

n = int(input("Tabuada de:"))
x = 1

while x <= 10:
    tabuada = n * x
    print(f"{n}x{x}={tabuada}")
    x = x + 1
    
