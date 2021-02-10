ca = cd = cg = 0
while True:
    x = 0
    while x > 4 or x < 1:
        x = int(input())
    if x == 1:
        ca += 1
    elif x == 2:
        cg += 1
    elif x == 3:
        cd += 1
    elif x == 4:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(ca))
print('Gasolina: {}'.format(cg))
print('Diesel: {}'.format(cd))