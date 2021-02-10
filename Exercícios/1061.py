dia = hora = minuto = segundo = 0
n, d = input().split(' ')
di = int(d)
X, Y, Z = input().split(' : ')
hi = int(X)
mi = int(Y)
si = int(Z)
z, d = input().split(' ')
df = int(d)
A, B, C = input().split(' : ')
hf = int(A)
mf = int(B)
sf = int(C)
if di == df:
    dia = 0
    if hi == hf:
        hora = 0
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mf > mi:
            minuto = mf - mi
    if hi < hf:
        hora = hf - hi
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mi > mf:
            hora = hora - 1
            minuto = (60-mi) + mf
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
        if mf > mi:
            minuto = mf - mi
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
if di > df:
    dia = (30-di) + df
    if hi == hf:
        hora = 0
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mf > mi:
            minuto = mf - mi
    if hi < hf:
        hora = hf - hi
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mi > mf:
            hora = hora - 1
            minuto = (60-mi) + mf
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
        if mf > mi:
            minuto = mf - mi
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
if df > di:
    dia = df - di
    if hi == hf:
        hora = 0
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mf > mi:
            minuto = mf - mi
    if hi < hf:
        hora = hf - hi
        if mi == mf:
            minuto = 0
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
        if mi > mf:
            hora = hora - 1
            minuto = (60-mi) + mf
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
        if mf > mi:
            minuto = mf - mi
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
    if hi > hf:
        dia = dia - 1
        hora = (24-hi) + hf
        if mi == mf:
            minuto = 0
        if mi > mf:
            hora = hora - 1
            minuto = (60-mi) + mf
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-si) + sf
        if mi < mf:
            minuto = mf - mi
            if si == sf:
                segundo = 0
            if sf > si:
                segundo = sf - si
            if si > sf:
                minuto = minuto - 1
                segundo = (60-sf) + si
print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundo))
