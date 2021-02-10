x = int(input())
y = int(input())
if y > x:
    c = y
    y = x
    x = c
y += 1
while y < x:
    if y % 5 == 2 or y % 5 == 3:
        print(y)
    y += 1

