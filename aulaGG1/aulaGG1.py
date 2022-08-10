""" laço c no intervalo (1-10)
    passo """

"""i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))


for c in range(i, f + 1, p):
    print(c)

print('FINISH')"""

"""s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'Resultado da soma dos valores: {s}')"""

#Desafio 1

"""for c in range(10, 0, -1):
    print(c)
print('BUMM!')"""

#Desafio 2

"""
for c in range(2, 52, 2):
    print(c)"""

#Desafio 3

s = 0

for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print(s)