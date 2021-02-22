import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')

while True:
    try:
        x = int(input())
        moedas = []
        c = ('’')
        for _ in range(x):
            moeda = int(input())
            moedas.append(moeda)
        passo = int(input())
        soma=0
        for z in range(x-1, -1, -passo):
            soma += moedas[z]
        primo = 0
        if soma == 1:
            print("Bad boy! I’ll hit you.")
        else:
            for i in range(1, soma+1):
                if soma % i ==0:
                    primo += 1
            if primo > 2:
                print("Bad boy! I" + c +"ll hit you.")
            else:
                print("You" + c + "re a coastal aircraft, Robbie, a large silver aircraft.")
    except EOFError:
        break


