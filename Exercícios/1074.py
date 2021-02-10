inegativo = pnegativo = ipositivo = ppositivo = 0
zero = 0
repeticoes = int(input())
for i in range(0, repeticoes):
    c = int(input())
    if c > 0:
        if c %2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif c < 0:
        if c % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    else:
        print('NULL')
