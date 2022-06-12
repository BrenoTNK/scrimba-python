python = {
    'John'    : 35,
    'Eric'    : 36,
    'Michael' : 35,
    'Terry'   : 38,
    'Graham'  : 37,
    'TerryG'  :34
}

holy_grail = {
    'Arthur'       : 40,
    'Galahad'      : 35,
    'Lancelot'     : 39,
    'Knight of NI' : 40,
    'Zoot'         : 17
}

life_of_brian = {
    'Brian'         : 33,
    'Reg'           : 35,
    'Stan/Loretta'  : 32,
    'Biccus Diccus' : 45
}

print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('Ele não está aqui')

pessoa = {}
pessoa1 = {}
pessoa2 = {}

    # Metodo 1;
pessoa.update(python)
pessoa.update(holy_grail)
pessoa.update(life_of_brian)
print(sorted(pessoa.items()))

    # Metodo 2;
for grupo in (python, holy_grail) : pessoa1.update(grupo)
print(sorted(pessoa1.items()))

    # Metodo 3;
pessoa2 = {**python, **holy_grail, **life_of_brian}
print(sorted(pessoa2.items()))
print('A soma das idade: ', sum(pessoa.values()))