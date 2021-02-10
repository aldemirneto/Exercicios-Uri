while True:
    lista = []
    lista.clear()
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(1, x+1):
            lista.append(i)
        for c in range(1, x+1):
            if c == x:
                print(c)
            else:
                print(c, end=' ')