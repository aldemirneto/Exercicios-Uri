c = int(input())
i = inicio = 0
inicio2 = 1
print(inicio, inicio2, end=' ')
while True:
    y = inicio2
    inicio2 += inicio
    inicio = y
    i += 1
    if i == (c-2):
        print(inicio2)
        break
    else:
        print(inicio2, end=' ')
