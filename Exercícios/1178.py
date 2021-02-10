Numero = float(input())
divide = []
for i in range(0, 99+1):
    divide.append(Numero)
    Numero = (Numero/2)
for c in range(0, 99+1):
    print('N[{}] = {:.4f}'.format(c, divide[c]))
