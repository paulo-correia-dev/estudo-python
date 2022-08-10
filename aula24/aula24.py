lista = [
    ['Paulo', 'Correia', 'Paulinho'],
    ['Nome', 'Sobrenome', 'Pseudônimo'],
    ['Barbara', 'Gabriela', 'Moreira']
]

for v1, v2 in enumerate(lista, 53):
    print(v1, 'agora ', v2)

"""enumerada = list(enumerate(lista))
print(enumerada[0][1][2])"""

"""
[ <-- enumerate
     0  1
    (0, ['Paulo', 'Correia', 'Paulinho']),  # 0
    (1, ['Nome', 'Sobrenome', 'Pseudônimo']),  # 1
    (2, ['Barbara', 'Gabriela', 'Moreira'])  # 2
]
"""