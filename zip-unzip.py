'''
nums = '1234'
letras = ['a','b', 'c', 'd']
nomes = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

# combo = zip(nums, letras)
# print(combo)

# combo = list(zip(nums, letras))
# print(combo)

# combo = list(zip(nums, letras, nomes))
# print(combo)
# num,let,nom = zip(*combo)
# print(num,let,nom)
'''

chave = 'this parrot is deceased'
valor = 'denna papegojan är avliden'

chave = chave.split()
valor = valor.split()
print(chave, valor)

dicionario = dict(zip(chave, valor))
print(dicionario)

novo_dicionario = {
    chave:valor for chave, valor in zip(chave, valor)
}
print(novo_dicionario)

en,sv = list(dicionario.keys()), list(dicionario.values())
print(en,sv)

en1,sv1 = zip(*dicionario.items())
print(en1,sv1)