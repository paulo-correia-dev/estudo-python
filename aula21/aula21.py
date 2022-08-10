"""variavel = 'Valor'

#         0    1         2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#        -6      -5     -4   -3   -2     -1

lista[5] = 'Qualquer outra coisa'

string = 'ABCDE'


print(lista[1:4])"""

"""l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.append('b')
print(l2[3])

l1.insert(0, 'paulo')


print(l1[0])
print(l1)
print(l2)

l1.pop(0)

print(l1)"""

"""l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l3.insert(0, 'Paulo')
del(l3[2:5])
print(l3)
del(l3[0])
print(l3)"""

"""l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l3))
print(min(l3))"""

"""l4 = list(range(0, 10, 3))


for valor in l4:
    print(valor)"""

"""l2 = ['String', True, 10, -20.5]

for e in l2:
    print(f'O tipo de {e} é {type(e)}')"""

secreta = 'perfume'
digitadas = []

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra! ")

        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Tem essa letra {letra}')
        print(secreta)
    else:
        print(f'NÃO tem essa letra {letra}')
        print(secreta)
        digitadas.pop()

    secreta_temp = ''

    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '*'

    if secreta_temp == secreta:
        print('Ganhou!')
        break
    else:
        print(secreta_temp)
