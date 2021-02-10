par =[]
impar = []
for i in range(0, 15):
    numero = int(input())
    if numero %2 == 0:
        par.append(numero)
        if len(par) >= 5:
            for i in range(0, len(par)):
                print('par[{}] = {}'.format(i, par[i]))
            par.clear()
    if numero % 2 != 0:
        impar.append(numero)
        if len(impar) >= 5:
            for i in range(0, len(impar)):
                print('impar[{}] = {}'.format(i, impar[i]))
            impar.clear()
for i in range(0, len(impar)):
    print('impar[{}] = {}'.format(i, impar[i]))
for i in range(0, len(par)):
    print('par[{}] = {}'.format(i, par[i]))