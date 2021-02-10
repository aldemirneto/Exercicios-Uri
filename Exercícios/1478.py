c = 0
while True:
    N = int(input())
    if N == 0:
        break
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(1)
        matriz.append(linha)
    valor = 1
    for i in range(N):
        for j in range(N):
            if j == i:
                matriz[i][j] = valor
    for i in range(N):
        for j in range(N):
            x = j+1
            if i == c:
                matriz[i][j] = x
    for i in range(N):
        for j in range(N):
            z = N - j
            if i == N - 1:
                matriz[i][j] = z
    for i in range(N):
        for j in range(N):
            z = N - j
            if j == N - 1:
                matriz[i][j] = z
    print(matriz)

