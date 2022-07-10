num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 5555
print(f'{num_2:0^10}')

num_4 = 1150
print(f'{num_2:.3f}')

num_5 = 1150
print(f'{num_2:0>10.3f}')

nome = 'PAULO CORREIA'
print(f'{nome:#^17}')

print(f'{len(nome)}')

nome_formatado = '{n:@>14}'.format(n=nome)
print(nome_formatado)


