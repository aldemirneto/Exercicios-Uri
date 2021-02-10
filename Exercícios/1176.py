inicio = 0
inicio2 = 1
i = 0
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
while True:
    y = inicio2
    inicio2 += inicio
    inicio = y
    i += 1
    if i == 60:
        break
    else:
       fibonacci.append(inicio2)
print(fibonacci)
c = int(input())
for i in range(0, c):
    numero = int(input())
    print('Fib({}) = {}'.format(numero, fibonacci[numero]))