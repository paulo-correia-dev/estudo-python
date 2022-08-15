frutas = ('morango', 'limao', 'abacate', 'abacaxi', 'laranja', 'pessego', 'manga', 'mexirica', 'maca', 'pera')

"""for cont in frutas:
    vogais = ''
    for cont2 in cont:
        if cont2 == 'a' or cont2 == 'e' or cont2 == 'i' or cont2 == 'o' or cont2 == 'u':
            vogais += cont2 + ' '
    print(f'Vogais da palavra {cont}: {vogais}')"""


for fruta in frutas:
    print(f'\nNa palavra {fruta.upper()}, temos as vogais: ', end='')
    for letra in fruta:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
