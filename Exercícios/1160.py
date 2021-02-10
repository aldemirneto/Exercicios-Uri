testes = int(input())
for c in range(0, testes):
    anos = 0
    C1, C2, T1, T2 = input().split(' ')
    c1 = int(C1)
    c2 = int(C2)
    t1 = float(T1)
    t2 = float(T2)
    while c1 <= c2:
        c1 *= (1 + (t1 / 100))
        c1 = int(c1)
        c2 *= (1 + (t2 / 100))
        c2 = int(c2)
        anos += 1
        if anos >= 101:
            print('Mais de 1 seculo.')
            break
    if anos <=100:
        anos = int(anos)
        print('{} anos.'.format(anos))
