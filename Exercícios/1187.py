soma = 0
Matriz = []
indice = 0
operacao = input().strip().upper()
for i in range(0, 12):
    linha=[]
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    Matriz.append(linha)
for a in range(0, 6):
    inicio = a
    final = 11 - a
    for b in range(inicio+1, final):
        if a == indice:
            soma += Matriz[a][b]
    indice += 1
if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))