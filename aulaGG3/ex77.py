frutas = ('morango', 'limao', 'abacate', 'abacaxi', 'laranja', 'pessego', 'manga', 'mexirica', 'maca', 'pera')

for cont in frutas:
    vogais = ''
    for cont2 in cont:
        if cont2 == 'a' or cont2 == 'e' or cont2 == 'i' or cont2 == 'o' or cont2 == 'u':
            vogais += cont2 + ' '
    print(f'Vogais da palavra {cont}: {vogais}')
