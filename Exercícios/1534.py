while True:
  try:
    matriz = []
    n = int(input())
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(3)
        matriz.append(linha)
    for i in range(n):
        for j in range(n):
            if i == j:
                matriz[i][j] = 1
    for i in range(n):
        for j in range(n):
            z = (n-1) - j
            if i == z:
                matriz[i][j] = 2

    for i in range(n):
        for j in range(n):
            if j == n-1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end='')

  except EOFError:
    break