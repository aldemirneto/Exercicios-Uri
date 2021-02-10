# -*- coding: utf-8 -*-

n, m = input().split('.')
n = float(n)
m = float(m)
n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1

m50 = m // 50
m = m - m50 * 50
m25 = m // 25
m = m - m25 * 25
m10 = m // 10
m = m - m10 * 10
m005 = m // 5
m = m - m005 * 5
m001 = m // 1
m = m - m001 * 1

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(n100))
print('{:.0f} nota(s) de R$ 50.00'.format(n50))
print('{:.0f} nota(s) de R$ 20.00'.format(n20))
print('{:.0f} nota(s) de R$ 10.00'.format(n10))
print('{:.0f} nota(s) de R$ 5.00'.format(n5))
print('{:.0f} nota(s) de R$ 2.00'.format(n2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(n1))
print('{:.0f} moeda(s) de R$ 0.50'.format(m50))
print('{:.0f} moeda(s) de R$ 0.25'.format(m25))
print('{:.0f} moeda(s) de R$ 0.10'.format(m10))
print('{:.0f} moeda(s) de R$ 0.05'.format(m005))
print('{:.0f} moeda(s) de R$ 0.01'.format(m001))