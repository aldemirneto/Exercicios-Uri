num = int(input())
referencia = 0
menorvalor = 9999
posicao = 0
numeros = input().split()
for c in range(0, len(numeros)):
    referencia = int(numeros[c])
    if referencia < menorvalor:
        menorvalor = referencia
        posicao = c
print('Menor valor: {}'.format(menorvalor))
print('Posicao: {}'.format(posicao))
