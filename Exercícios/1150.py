i = 1
s = 1
x = int(input())
z = x - 1
soma = x
while z <= x:
    z = int(input())
while z >= x:
    z -= x+s
    if soma >= x:
        s += 1
        i += 1

print(i)


