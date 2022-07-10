print('Crie uma conta \n')
usuario_create = input('Usuário: ')
senha_create = input('Senha: ')
print()
print('Acesse sua conta \n')
usuario_login = input('Usuário: ')
senha_login = input('Senha: ')

if (usuario_login == usuario_create) and (senha_login == senha_create):
    print('Você está dentro!')
else:
    print('Usuário ou senha incorretos!')
