print('Você deverá digitar 4 valores a seguir.'),

valores = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto e último número: ')))

# print(f'Você digitou os valores {valores[1:]}')

print('Você digitou os valores: ', end='')

for cont in valores:
    print(cont, end=' ')

print(f'\nO valor 9 apareceu {valores.count(9)} vezes.')

if 3 not in valores:
    print(f'Você não digitou o número  3, por isso ele não se encontra em nenhuma posição.')

else:
    print(f'A primeira ocorrência do valor 3 foi na {valores.index(3)+1}ª posição.')

print(f'Você digitou o(s) número(s) par(es):', end=' ')

for cont in valores:
    if cont % 2 == 0:
        print(cont, end=' ')
