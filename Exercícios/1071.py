s1: int
s1 = s2 = 0
c = int(input())
d = int(input())
if c > d:
    maior = c
    menor = d
else:
    maior = d
    menor = c
for i in range(menor+1, maior, 1):
    if i % 2 != 0:
        print('ponto')
        s1 += i
print(s1)
