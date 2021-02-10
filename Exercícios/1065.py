contapar = 0
for i in range(0, 5):
    numero = int(input())
    if numero % 2 == 0:
        contapar +=1
print('{} valores pares'.format(contapar))