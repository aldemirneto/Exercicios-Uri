A, B, C, D = input().split(' ')
n1 = int(A)
n2 = int(B)
n3 = int(C)
n4 = int(D)
if n1 == n2 == n3 == n4:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
if n1 > n3:
    s1 = (n1 * 60) + n2
    s2 = ((n3+24) * 60) + n4
    comparativo = s2 - s1
    r = (s2 - s1) % 60
    t = (s2 - s1) // 60
    if 1 <= comparativo <= 1440:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(t, r))
if n3 > n1:
    s1 = (n1 * 60) + n2
    s2 = (n3 * 60) + n4
    comparativo = s2 - s1
    r = (s2 - s1) % 60
    t = (s2 - s1) // 60
    if 1 <= comparativo <= 1440 :
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(t, r))
