continua = True
grenais = inter = gremio = empates = 0
while continua is True:
    X, Y = input().split(' ')
    gi = int(X)
    gg = int(Y)
    if gi > gg:
        inter += 1
    elif gg > gi:
        gremio += 1
    else:
        empates += 1

    while True:
        print('Novo grenal (1-sim 2-nao)')
        novo = int(input())
        if novo == 1:
            continua = True
            break
        else:
            continua = False
            break
    grenais += 1
print('{} grenais'.format(grenais))
print('Inter: {}'.format(inter))
print('Gremio: {}'.format(gremio))
print('Empates: {}'.format(empates))
if inter > gremio:
    print('Inter venceu mais')
else:
    print('Gremio venceu mais')