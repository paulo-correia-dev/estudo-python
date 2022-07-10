# While em Python - Laço de repetição

"""
nome = input('Qual o seu nome? ')
print(f'Seu nome é {nome}, você não pode logar.')

while nome != 'Paulo':
    nome = input('Qual o seu nome? ')
    if nome != 'Paulo':
        print(f'Seu nome é {nome}, você não pode logar.')

print('Bem vindo, Paulo!')
"""

"""
x = 0

while x <= 10:
    if x == 3:
        x = x + 1
        break  # continue

    print(x)
    x = x+1

print("Acabou")
"""
"""
x = 0  # coluna
y = 0  # linha

while x < 10:

    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1  # x = x+1

print('acabou')
"""
pergunta = "s"
while pergunta == "s":
    print()

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    num_1 = float(num_1)
    num_2 = float(num_2)
    operador = input('Digite um operador: ')

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador Inválido')

    pergunta = input('Deseja efetuar outra operação? [s]im, [n]ão.')

    if pergunta == 'n':
        break
