produtosPrecos = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2,
                  'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('-' * 40)

for cont in range (0, len(produtosPrecos)):
    if cont % 2 == 0:
        print(f'{produtosPrecos[cont] :*<30}', end= '')
    else:
        print(f'R$ {produtosPrecos[cont]: >7.2f}')
print('-' * 40)