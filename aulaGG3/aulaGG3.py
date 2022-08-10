from random import randint

"""numeros = []

for cont in range(0, 5):
    aleatorio = random.randint(0, 100)
    numeros.append(aleatorio)

numeros = tuple(sorted(numeros))

print(f'Cinco números aleatórios: {numeros}')
print(f'Menor valor: {min(numeros)}')
print(f'Maior valor: {max(numeros)}')"""

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Cinco números aleatórios: ', end='')

for cont in numeros:
    print(f'{cont}', end=' ')

print(f'\nMenor valor: {min(numeros)}')
print(f'Maior valor: {max(numeros)}')
