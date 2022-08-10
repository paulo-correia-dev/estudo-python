variavel = ['Paulo Correia', 'Barbara Correia', 'Casamento']

comeca_com_j: False

for valor in variavel:
    if valor.lower().startswith('b'):
        comeca_com_j = True
        print('Começa com B')
else:
    print('Não existe uma palavra que começa com B')
