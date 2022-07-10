nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
"""idade_limite = 18  # Idade limite para pegar empréstimo

if int(idade) >= idade_limite:
    print(f'{nome}, pode pegar empréstimo!')
else:
    print(f'{nome}, NÃO pode pegar empréstimo!')
"""

if 20 <= idade <= 30:
    print('Pode pegar empréstimo')
elif idade < 20:
    print(f'{nome}, você tem apenas {idade} anos, faltam {20 - idade} ano(s) para completar a idade mínima de 20 anos.')
elif idade > 30:
    print(f''
          f'{nome}, você tem {idade} anos, já se passaram (passou) {idade - 30} ano(s) da idade máxima de 30 anos.')
