c = int(input())
if c % 2 == 0:
    c += 1
for i in range(0, 12, 2):
    print(c)
    c = c + 2