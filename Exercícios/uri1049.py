resultado = str
animal1 = str(input())
if animal1 == 'vertebrado':
    animal2 = str(input())
    if animal2 == 'ave':
        animal3 = str(input())
        if animal3 == 'carnivoro':
            resultado = 'aguia'
        else:
            resultado = 'pomba'
    else:
        animal3 = str(input())
        if animal3 == 'onivoro':
            resultado = 'homem'
        else:
            resultado = 'vaca'
else:
    animal2 = str(input())
    if animal2 == 'inseto':
        animal3 = str(input())
        if animal3 == 'hematofago':
            resultado = 'pulga'
        else:
            resultado = 'lagarta'
    else:
        animal3 = str(input())
        if animal3 == 'hematofago':
            resultado = 'sanguessuga'
        else:
            resultado = 'minhoca'

print(resultado)