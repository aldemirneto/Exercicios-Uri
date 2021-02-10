lista = []
for c in range(0, 10):
    lista.append(int(input()))
for c in range(0, len(lista)):
    if lista[c] <= 0:
        lista[c] = 1
for i in range(0, len(lista)):
    print('X[{}] = {}'.format(i, lista[i]))