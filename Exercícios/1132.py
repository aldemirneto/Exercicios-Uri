x = int(input())
y = int(input())
soma = 0
if y > x:
    c = y
    y = x
    x = c
while y <= x:
    if y % 13 != 0:
        soma += y
    y += 1
print(soma)
