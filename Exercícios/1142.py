c = int(input())
limite = c * 4
for i in range(1, limite+1):
    if i %4 == 0:
        print('PUM', end='\n')
    else:
        print(i, end=' ')