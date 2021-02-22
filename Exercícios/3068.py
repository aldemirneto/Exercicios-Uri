contameteoro = 0
c = 0
while True:
    cont = 0
    X1, Y1, X2, Y2 = input().split(' ')
    x1 = int(X1)
    x2 = int(X2)
    y1 = int(Y1)
    y2 = int(Y2)
    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        break
    else:
        if x1 > x2:
            c = x2
            x2 = x1
            x1 = c
        if y2 > y1:
            c = y1
            y1 = y2
            y2 = c
        m = int(input())
        for i in range(m):
            meteoro = input().split()
            if (x2 >= int(meteoro[0]) >= x1) and (y1 >= int(meteoro[1]) >= y2):
                cont += 1
    c += 1
    print(f'Teste {c}')
    print(cont)

