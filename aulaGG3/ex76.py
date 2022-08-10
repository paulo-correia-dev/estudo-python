produtosPrecos = ('Lapis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2,
                  'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

contador = 0
traco = '-'
frase = 'Listagem de Preço'
print(f'{traco :-^29}')
print(f'{frase : ^29}')
print(f'{traco :-^29}')

while contador < len(produtosPrecos):

    print(f'{produtosPrecos[contador] :*<20}R$', end=' ')
    contador += 1
    print(f'{produtosPrecos[contador]: >6}')
    contador += 1

print(f'{traco :-^29}')
