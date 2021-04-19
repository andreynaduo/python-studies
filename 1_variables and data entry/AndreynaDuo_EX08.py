a = 4
b = 2

expressao1 = (a/b)+(b/a)
expressao2 = a/b + b/a
print(expressao1 == expressao2)

expressao3 = a/(b+b)/a
expressao4 = a/b+b/a
print(expressao3 == expressao4)

expressao5 = (a+b)*b-a
expressao6 = a+b*b-a
print(expressao5 == expressao6)

#sei que eu poderia ter simplesmente colocado as expressões direto
#e ficaria muito mais simples
#porém fiz assim para treinar variáveis :)

