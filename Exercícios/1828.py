'''
1. a tesoura corta o papel;
2. o papel embrulha a pedra;
3. a pedra esmaga o lagarto;
4. o lagarto envenena Spock;
5. Spock destrói a tesoura;
6. a tesoura decapita o lagarto;
7. o lagarto come o papel;
8. o papel contesta Spock;
9. Spock vaporiza a pedra;
10. a pedra quebra a tesoura.
'''




c = int(input())
for i in range(c):
    x, y = input().split(' ')
    if (x == 'tesoura' and y == 'papel') or (x == 'papel'and y == 'pedra') or(x == 'pedra'and y == 'lagarto') or(x == 'lagarto' and y == 'Spock') or(x == 'Spock' and y == 'tesoura') or (x == 'tesoura' and y == 'lagarto') or (x == 'lagarto' and y == 'papel')or (x=='papel' and y == 'Spock') or (x=='Spock' and y == 'pedra') or (x == 'pedra' and y == 'tesoura'):
        print('Caso #{} Bazinga!'.format(i+1))
    elif x == y:
        print('Caso #{} De novo!'.format(i+1))
    else:
        print('Caso #{} Raj trapaceou!'.format(i+1))