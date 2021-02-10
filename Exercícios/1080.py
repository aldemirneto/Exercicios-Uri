comparativo = position = 0
for c in range(0, 10):
    numero = int(input())
    if numero > comparativo:
        comparativo = numero
        position = (c+1)
print(comparativo)
print(position)
