""" PRIMEIRO EXERCÍCIO

numero = input('Digite um número inteiro: ')

if numero.isdecimal():
    numero = int(numero)
    resto_divisao = numero % 2

    if resto_divisao == 0:
        print(f'{numero} é par.')
    else:
        print(f'{numero} é ímpar.')

else:
    print(f'[ERROR] O valor inserido não é um número inteiro!')
"""

""" SEGUNDO EXERCÍCIO
horas = input('Digite as horas no formaro 24 hrs sem os minutos! EX: "12" . (Meio Dia) \n')

if horas.isdecimal():
    horas = int(horas)

    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
else:
    print('[ERROR] Você não escreveu as horas conforme o indicado.')
"""

# EXERCÍCIO 3

nome = input('Escreva seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é grande!')
