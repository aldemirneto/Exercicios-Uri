matriz = []
soma1 = soma2 = soma = 0
indice = contador = 0
indice2 = 6
operacao = input()

for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
for a in range(0, 6):
    c = a
    for b in range(0, c):
        if a == indice:
            soma1 += matriz[a][b]
    indice += 1
for a in range(6, 12):
    z = (5 - contador)
    for x in range(0, z):
        if a == indice2:
            soma2 += matriz[a][x]
    contador += 1
    indice2 += 1

soma = soma1 + soma2

if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))