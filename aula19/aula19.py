#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < len(frase):
    letra = frase[contador]
    if letra == 'r':
        nova_string = nova_string + 'R'
    else:
        nova_string = nova_string + letra
    contador += 1
print(nova_string)
