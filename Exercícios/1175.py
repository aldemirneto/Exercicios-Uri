lista = []
z = 0
j = 9
for i in range(0, 10):
    lista.append(int(input()))
while z < j:
    c = lista[z]
    lista[z] = lista[j]
    lista[j] = c
    z += 1
    j -= 1
print(lista)
