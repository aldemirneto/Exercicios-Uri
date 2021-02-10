x = input().split(' ')
dia1, dia2, dia3 = int(x[0]), int(x[1]), int(x[2])
constante = 0
comparativo = 0
if dia1 == dia2:
    if dia3 <= dia2:
        print(':(')
    else:
        print(':)')
elif dia2 > dia1:
    constante = dia2 - dia1
    if (dia3 == dia2) or (dia3 < dia2):
        print(':(')
    else:
        comparativo = dia3 - dia2
        if comparativo < constante:
            print(':(')
        else:
            print(':)')
elif dia1 > dia2:
    constante = dia1 - dia2
    if dia3 > dia2:
        print(':)')
    else:
        comparativo = dia2 - dia3
        if comparativo >= constante:
            print(':(')
        else:
            print(':)')


