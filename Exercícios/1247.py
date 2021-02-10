import math
while True:
    try:
        PF = 12
        x = input().split()
        d, vf, vg = int(x[0]), int(x[1]), int(x[2])
        h = math.sqrt((PF*PF) + (d*d))
        tf = PF/12
        tg = h/vg

        if tg > tf:
            print('N')
        else:
            print('S')
    except EOFError:
        break