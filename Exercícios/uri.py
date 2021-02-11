dist = [9999]
total = [9999]
while True:
    try:
        dist.clear()
        total.clear()
        n, k = input().split(' ')
        N = int(n)
        K = int(k)
        dist[0] = 0
        total[0] = 0
        for i in range(1, N):
            dist.append(int(input()))
            total.append(dist[i] - dist[i - 1])
        for i in range(0, N):
            if total[i] == 1:
                total[i] = 0
        total.sort(reverse=True)
        soma = 0
        for i in range(0, N):
            soma = soma + total[i]
        print(soma)
    except EOFError:
        break
