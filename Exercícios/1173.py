lista = []
c = int(input())
for i in range(0, 10):
    lista.append((c))
    c = c * 2
for i in range(0, len(lista)):
    print('N[{}] = {}'.format(i, lista[i]))