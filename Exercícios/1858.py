menor = 9999999
posicao = 0
x = int(input())
carrascos = input().split()
for i in range(x):
    c = int(carrascos[i])
    if c < menor:
        menor = c
        posicao = i
print(posicao+1)