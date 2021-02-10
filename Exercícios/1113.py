lista = []
while True:
    M, N = input().split(' ')
    n1 = int(M)
    n2 = int(N)
    if n1 == n2:
        break
    else:
        if n1 > n2:
            lista.append('Decrescente')
        else:
            lista.append('Crescente')
for i in range(0, len(lista)):
    print(lista[i])