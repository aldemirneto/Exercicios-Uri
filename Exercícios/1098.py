i = 0
while i < 2:
    j = i + 1
    for a in range(0, 3):
        if j != int(j):
            print('I={:.1f} J={:.1f}'.format(i, j))
        else:
            print('I={:.0f} J={:.0f}'.format(i, j))
        j += 1
    i += 0.2
