i = 1
while i <= 9:
    j = i + 6
    n = j - 2
    while j >= n:
        print('I={} J={}'.format(i, j))
        j -= 1
    i += 2