print('Você deverá digitar 4 valores a seguir.'),

valores = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto e último número: ')))

# print(f'Você digitou os valores {valores[1:]}')

print('Você digitou os valores: ', end='')

for cont in valores:
    print(cont, end=' ')

print(f'\nO valor 9 apareceu {valores.count(9)} vezes.')

if valores.count(3) == 0:
    print(f'Você não digitou o número  3, por isso ele não se encontra em nenhuma posição.')
else:
    if valores.index(3) == 0:
        print(f'A primeira ocorrência do valor 3 foi na 1ª posição.')
    elif valores.index(3) == 1:
        print(f'A primeira ocorrência do valor 3 foi na 2ª posição.')
    elif valores.index(3) == 2:
        print(f'A primeira ocorrência do valor 3 foi na 3ª posição.')
    elif valores.index(3) == 3:
        print(f'A primeira ocorrência do valor 3 foi na 4ª posição.')

numerosPares = 0

for cont in valores:
    if cont % 2 == 0:
        numerosPares += 1

if numerosPares == 0:
    print(f'Você não digitou nenhum número par.')
else:
    print(f'Você digitou {numerosPares} número(s) par(es).')