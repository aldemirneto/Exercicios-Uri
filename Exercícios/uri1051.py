salario = float(input())
if salario <= 2000.00:
    print('Isento')
    i = 0

if 2000.00 < salario <= 3000.00:
    salario8 = (salario - 2000)
    i = salario8 * 0.08

if 3000.00 < salario <= 4500.00:
    i8 = 80
    salario18 = salario-3000
    i = salario18 * 0.18 +i8

if salario > 4500.00:
    i8 = 80
    i18 = 270
    salario28 = salario-4500
    i = i18 + i8 + (salario28 * 0.28)
if salario > 2000:
    i = float(i)
    print('R$ {:.2f}'.format(i))