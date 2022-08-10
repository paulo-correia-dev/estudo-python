# Existem 3 tipos de variáveis que armazenam vários valores: tuplas, listas e dicionários

# As tuplas são IMUTÁVEIS

"""lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))  # coloca em ordem

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c}, na posição {pos}!')
print('Comi tudo!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

pessoa = ('Paulo', 21, 'M', 70.00)
print(pessoa)
del pessoa"""


"""num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num1 = int(input('Digite um número entre 0 e 20: '))

while num1 < 0 or num1 > 20:
    print('O número digitado não está entre 0 e 20.')
    num1 = int(input('Tente novamente! Digite um número entre 0 e 20: '))

for cont in range(0, len(num)):

    if num1 == cont:
     print(f'Você digitou o número {num[cont]}.')"""


"""brasileiro = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Internacional', 
'Atlético-MG', 'Bragantino', 'América-MG' 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará', 'Coritiba', 'Avaí', 
'Fortaleza', 'Cuiabá', 'Atlético-GO', 'Juventude') 

print(brasileiro[0:5])
print(brasileiro[-4:])
print(sorted(brasileiro))
time = input('Digite o nome do time e veja sua posição: ')
print(f'O time {time} está na posição {brasileiro.index(time)}')"""
