matriz = []
indice = 0
soma = 0
operacao = input()
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
for a in range(0, 12):
    c = (11-a)
    for b in range(c+1, 12):
        if a == indice:
            soma += matriz[a][b]
    indice += 1
if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/66))