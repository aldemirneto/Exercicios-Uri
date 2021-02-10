a = float(input())
p = rg = 0
if 0 < a <= 400.00:
    ns = a
    p = 15
    s = (p/100) + 1
    a = a * s
    rg = a - ns
elif 400.01 <= a <= 800.00:
    ns = a
    p = 12
    s = (p / 100) + 1
    a = a * s
    rg = a - ns
elif 800.01 <= a <= 1200.00:
    ns = a
    p = 10
    s = (p / 100) + 1
    a = a * s
    rg = a - ns
elif 1200.01 < a <= 2000.00:
    ns = a
    p = 7
    s = (p / 100) + 1
    a = a * s
    rg = a - ns
elif a > 2000.00:
    ns = a
    p = 4
    s = (p / 100) + 1
    a = a * s
    rg = a - ns
print('Novo salario: {:.2f}'.format(a))
print('Reajuste ganho: {:.2f}'.format(rg))
print('Em percentual: {} %'.format(p))
