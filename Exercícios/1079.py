c = int(input())
for i in range(0, c):
    A, B, C = input().split(' ')
    a = float(A)
    b = float(B)
    c = float(C)
    media = ((a*2) + (b*3) + (c*5))/10
    print('{:.1f}'.format(media))