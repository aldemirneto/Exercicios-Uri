i, contapasso, j, d, e = 0, 0, 0, 0, 0
x = int(input())
referencia = []
numero = input().split()
for z in range(x):
    numero[z] = int(numero[z])
for _ in range(x):
    referencia.append(0)
while True:
    if i >= x or i < 0:
        break
    elif numero[i] == 0:
        referencia[i] = 1
        i -= 1
    else:
        if numero[i] % 2 == 0:
            numero[i] -= 1
            if referencia[i] == 0:
                d += 1
            referencia[i] = 1
            print(referencia)
            i -= 1

        elif numero[i] % 2 != 0:
            numero[i] -= 1
            if referencia[i] == 0:
                d += 1
            referencia[i] = 1
            print(referencia)
            i += 1

for i in range(len(numero)):
    contapasso += numero[i]
print('{} {}'.format(d, contapasso), end='\n')