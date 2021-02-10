total = totalc = totalr = totals = pctc = pctr = pcts = 0

c = int(input())
for i in range(0, c):
    numero, tipo = input().split(' ')
    total += int(numero)
    if tipo == 'S':
        totals += int(numero)
    if tipo == 'C':
        totalc += int(numero)
    if tipo == 'R':
        totalr += int(numero)
pctc = (totalc*100)/total
pctr = (totalr*100)/total
pcts = (totals*100)/total
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(totalc))
print('Total de ratos: {}'.format(totalr))
print('Total de sapos: {}'.format(totals))
print('Percentual de coelhos: {:.2f} %'.format(pctc))
print('Percentual de ratos: {:.2f} %'.format(pctr))
print('Percentual de sapos: {:.2f} %'.format(pcts))