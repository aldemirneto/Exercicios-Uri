lista = []
c = nota = 0
while True:
    x = float(input())
    if x >= 0 and x <= 10:
        nota += x
        c +=1
    else:
        lista.append('nota invalida')
    if c == 2:
        break
media =nota / 2
for i in range(0, len(lista)):
    print(lista[i])
print('media = {:.2f}'.format(media))