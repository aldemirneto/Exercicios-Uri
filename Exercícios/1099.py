impar = 0
c = int(input())
for i in range(0, c):
    impar = 0
    x, y = input().split(' ')
    n1 = int(x)
    n2 = int(y)
    if n2 > n1:
        c = n1
        n1 = n2
        n2 = c
    for z in range(n2, n1):
        if z % 2 != 0 and z != n2:
            impar += z
    print(impar)