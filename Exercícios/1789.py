while True:
    try:
        copia = []
        n = int(input())
        x = input().split()
        for c in range(len(x)):
            copia.append(int(x[c]))
        z = v = 0
        for c in range(len(x)):
            if copia[c] > z:
                z = copia[c]
        if z < 10:
            v = 1
        elif z >= 20:
            v = 3
        else:
            v = 2
        print(v)
    except EOFError:
        break