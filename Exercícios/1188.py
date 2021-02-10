soma = 0
Matriz = []
indice = 11
ponto = 0
operacao = input().strip().upper()
for i in range(0, 12):
    linha=[]
    for j in range(0, 12):
        numero = float(input())
        linha.append(numero)
    Matriz.append(linha)
for a in range(11, 6, -1):
    inicio = 12 - a
    final = a - 1
    for b in range(inicio, final+1):
        if a == indice:
            ponto +=1
            soma += Matriz[a][b]
    indice -= 1
if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))