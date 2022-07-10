"""
 = operador de atribuição
 == operador de igualdade
 variável é um apelido que dou pra algo que eu salvo na memoria do computador
"""

#  nome = 'Paulo'
#  print(nome, type(nome))

nome = 'Paulo Correia'
idade = 21
altura = 1.74
e_maior = idade > 18
peso = 70.8

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('Maior de Idade? ', e_maior)
print(idade * altura)

#  cálculo do IMC
print(nome, 'tem', idade, 'anos de idade e seu IMC é', peso/altura ** 2)
print(nome, 'tem', idade, 'anos de idade e seu IMC é', peso/(altura * altura))

