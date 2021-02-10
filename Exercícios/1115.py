lista = []
while True:
    px, py = input().split(' ')
    x = int(px)
    y = int(py)
    if x == 0 or y == 0:
        break
    else:
        if x > 0 and y > 0:
            lista.append('primeiro')
        elif x < 0 and y < 0:
            lista.append('terceiro')
        elif x > 0 and y < 0:
            lista.append('quarto')
        else:
            lista.append('segundo')
for i in range(0, len(lista)):
    print(lista[i])