#Escreva um programa que leia três números e que imprima o maior e o menor.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a > b:
    if a > c:
        print(f"{a} é o maior")
elif b > c:
        print(f"{b} é o maior")
else:
    print(f"{c} é o maior")

if a < b:
    if a < c:
        print(f"{a} é o menor")
elif b < c:
        print(f"{b} é o menor")
else:
    print(f"{c} é o menor")
    