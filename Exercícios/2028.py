i = 1
while True:
    try:

        x = int(input())
        print("\n")
        n = 1
        list = [0]
        if 0 < x < 2:
            list.append(1)
        elif x > 1:
            for c in range(x):
                for _ in range((c+1)):
                    list.append(c + 1)

        if len(list) < 2:
            print(f'Caso {i}: {len(list)} numero')
        else:
            print(f'Caso {i}: {len(list)} numeros')
        for z in range(len(list)):
            if z == (len(list)-1):
                print(list[z], end='')
            else:
                print(list[z], end=' ')
        print("\n")
        i += 1
    except EOFError:
        break
