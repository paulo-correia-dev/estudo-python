num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

# isnumeric( ) - isdigit() - isdecimal
# números e positivos
# print(num_1.isnumeric())
# print(num_2.isnumeric())

"""
if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
else:
    print('Não pude comverter os números.')
"""
# inteiros e positivos
"""
if num_1.isdecimal() and num_2.isdecimal():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
else:
    print('Não pude comverter os números.')
"""

if num_1.isnumeric() and num_2.isnumeric():
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 + num_2)
else:
    print('Não pude comverter os números.')