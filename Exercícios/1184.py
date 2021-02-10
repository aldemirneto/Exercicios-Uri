matriz = []
soma = 0
indice = 0
operacao = input()
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
for a in range(0, 12):
    c = indice
    for b in range(0, c):
        if a == indice:
            soma += matriz[a][b]
    indice +=1
if operacao == 'S':
    print('{:.1f}'.format(soma))
elif operacao == 'M':
    print('{:.1f}'.format(soma/66))