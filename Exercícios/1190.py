matriz = []
soma1 = soma2 = soma =subtrai = 0
indice =0
contador = 5
indice2 = 6
operacao = input()

for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
for a in range(0, 6):
    c = 11 - subtrai
    for b in range(c+1, 12):
        if a == indice:
            soma1 += matriz[a][b]
    subtrai += 1
    indice += 1
for a in range(6, 12):
    z = (12 - contador)
    for x in range(z, 12):
        if a == indice2:
            soma2 += matriz[a][x]
    contador -= 1
    indice2 += 1

soma = soma1 + soma2

if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))