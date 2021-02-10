contapositivo = contapar = contaimpar = contanegativo = 0
for c in range(0, 5):
    numero = int(input())
    if numero % 2 == 0:
        contapar += 1
    else:
        contaimpar += 1
    if numero > 0:
        contapositivo += 1
    elif numero < 0:
        contanegativo +=1

print('{} valor(es) par(es)'.format(contapar))
print('{} valor(es) impar(es)'.format(contaimpar))
print('{} valor(es) positivo(s)'.format(contapositivo))
print('{} valor(es) negativo(s)'.format(contanegativo))