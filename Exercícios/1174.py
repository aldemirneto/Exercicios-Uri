lista = []
for i in range(0, 10):
    lista.append(float(input()))
for i in range(0, len(lista)):
    if lista[i] <= 10:
        print('A[{}] = {}'.format(i, lista[i]))
