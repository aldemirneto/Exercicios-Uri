contapositivo = media = 0
for i in range(0, 6):
    numero = float(input())
    if numero > 0:
        media += numero
        contapositivo += 1
media = media / contapositivo
print('{} valores positivos'.format(contapositivo))
print(media)