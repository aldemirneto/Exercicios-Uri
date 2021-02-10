matriz = []
soma = 0
indice = int(input())
operacao = input()
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
for a in range(0, 12):
    for b in range(0, 12):
        if b == indice:
            soma += matriz[a][b]
if operacao == 'S':
    print('{:.1f}'.format(soma))
elif operacao == 'M':
    print('{:.1f}'.format(soma/12))