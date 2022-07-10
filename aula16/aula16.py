#       [012345678]
texto = 'Python S2'
#      -[987654321]
#     [0123456789]
url = 'www.google.com.br/'
#    -[         987654321]
print(url[:-1])

print(texto[0:2])

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[::3]  # pular de x em x
print(nova_string)
