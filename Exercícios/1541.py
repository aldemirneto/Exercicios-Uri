x = 1000
while True:
    x = input().split()
    if x == ['0']:
        break
    A, B, C = x
    A, B, C = int(A), int(B), int(C)
    acasa = A * B
    permitido = acasa * (100/C)
    total = permitido **(1/2)
    total = int(total)
    print(total)