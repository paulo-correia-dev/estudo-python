nome = 'Paulo Correia'
idade = 21
altura = 1.74
e_maior = idade > 18
peso = 70.8
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', peso/altura ** 2)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc: .2f}')  # .2 signfc 2 casas decm e f signfc que é float
print('{} tem {} anos de idade e seu IMC é {: .2f}'.format(nome, idade, imc))
print('{0} {1} tem {1} {0} anos de idade e seu IMC é {2: .2f}'.format(nome, idade, imc))
print('{n}  tem {i} anos de idade e seu IMC é {indmc: .2f}'.format(n=nome, i=idade, indmc=imc))  # parametros nomeados
