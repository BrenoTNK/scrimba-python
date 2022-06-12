    # Função normal;
def quadrado(x):
    return x*x

    # Mesma função em lambda;
quadrado1 = lambda x: x*x
print(quadrado1(3))

dobro  = lambda x,y: 2*x*y
print(dobro(2, 3))


def pessoa(nome, apelido):
    # Função normal;
    return nome.strip().title() + ':' + apelido.strip().title()
print(pessoa('jOão viTOR', 'JV'))

    # Função em lambda;
pessoa1 = lambda nome,apelido : nome.strip().title() + ':' + apelido.strip().title()
print(pessoa1('jOão viTOR', 'JV'))



monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
def f_nomes(nomes):
    return nomes.split(' ')
monty_python.sort(key = lambda nomes:nomes.split(' ')[-1])
print(monty_python)
monty_python.sort(key= f_nomes)
print(monty_python)