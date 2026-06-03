print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Os segmentos acima podem formar um triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Os segmentos acima podem formar um triângulo Isósceles")
    else:
        print("Os segmentos acima podem formar um triângulo Escaleno")
else:
    print("Os segmentos acima podem formar um triângulo")
