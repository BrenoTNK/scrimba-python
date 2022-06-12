def funcao(nome, idade = 28):
    print(f'Olá {nome}! Você tem {idade} anos!')

nome = input('Digite o seu nome: ')
funcao(nome.capitalize(), 31)
funcao('Maria')
