user = input('User: ')
qtd_car_user = len(user)
print(qtd_car_user)

if qtd_car_user <= 6:
    print('O mínimo de algarismos deve ser 8.')

usuario_1 = input('Digite algo: ')
usuario_2 = input('Digite algo de novo: ')
print(f'A quantidade total de caracteres de {usuario_1} e {usuario_2} é {len(usuario_1 + usuario_2)}')