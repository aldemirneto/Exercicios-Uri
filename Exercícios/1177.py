c = int(input())
z = 0
lista = []
for i in range(0, 1000):
    z = 0
    while z < c:
        lista.append(z)
        z += 1
for c in range(0, 1000):
    print('N[{}] = {}'.format(c, lista[c]))