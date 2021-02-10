lista = []
n = int(input())
for i in range(0, n):
    x, y = input().split(' ')
    n1 = int(x)
    n2 = int(y)
    if n2 == 0:
        lista.append('divisao impossivel')
    else:
        divisao = n1 / n2
        lista.append(divisao)
for c in range(0, len(lista)):
    print(lista[c])
    