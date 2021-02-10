while True:
    soma = 0
    M, N = input().split(' ')
    n1 = int(M)
    n2 = int(N)
    if n1 <= 0 or n2 <= 0:
        break
    else:
        if n2 > n1:
            c = n1
            n1 = n2
            n2 = c
        for c in range(n2, n1+1):
            soma += c
            print(c, end=' ')
        print('Sum={}'.format(soma))