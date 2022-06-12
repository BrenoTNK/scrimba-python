import random, string

lista_amigos = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(lista_amigos, 3))
random.shuffle(lista_amigos)
print(lista_amigos)


c_baixa = 'abcdefghijklmnopqrstuvwxyz'
c_alta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digitos = '0123456789'
letras_numeros = string.ascii_letters + string.digits
print(letras_numeros)

palavra = ''
for i in range(7):
    palavra = palavra + random.choice(letras_numeros)
print(palavra)

palavra1 = ''.join(random.sample(letras_numeros, 7))
print(palavra1)

palavra2 = random.choices(letras_numeros, k=7)
print(palavra2)