
testes = int(input())
for c in range(0, testes):
    numeros = 0
    x = int(input())
    for i in range(1, x):
        n = i
        if x % n == 0:
            numeros += i
    if numeros == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))


