nome = 'Paulo Correia'
idade = 21
altura = 1.74
peso = 70.0
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} de idade, mede {altura} de altura e pesa {peso}. {nome} nasceu em {ano_nascimento} e seu '
      f'IMC é {imc:.2f}') 

