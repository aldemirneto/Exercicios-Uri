x = input().split(' ')
a, b = int(x[0]), int(x[1])
q = r = 0
if b!=0:
    if a < 0 and b > 0:
        q = int(a/b) - 1
        r = a - (b*q)

    elif a > 0 and b < 0:
        q = int(a/b)
        r = a - (b*q)

    elif a > 0 and b > 0:
        q = int(a/b)
        r = a - (b*q)

    elif a < 0 and b < 0:
        q = int((a+b)/b)
        r = a - (b*q)


print('{} {}'.format(q, r))
