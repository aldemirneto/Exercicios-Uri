
testes = int(input())
for c in range(0, testes):
    numeros = 0
    x = int(input())
    for i in range(1, x+1):
        if x % i == 0:
            numeros += 1
    if numeros >= 3:
        print('{} nao eh primo'.format(x))
    else:
        print('{} eh primo'.format(x))


