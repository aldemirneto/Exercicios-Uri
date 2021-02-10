lista = []
c = nota = 0
continua = True
while continua == True:
    x = float(input())
    if x >= 0 and x <= 10:
        nota += x
        c +=1
        if c == 2:
            media =nota / 2
            print('media = {:.2f}'.format(media))
            while True:
                print("novo calculo(1-sim 2-nao)")
                novo = int(input())
                if novo == 2:
                    continua = False
                    break
                if novo == 1:
                    c = 0
                    nota = 0
                    continua = True
                    break
    else:
        print('nota invalida')

