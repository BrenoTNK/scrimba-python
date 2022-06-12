def funcao(nome, idade = 28, cor = 'verde'):
    print(f'Olá {nome}, você terá {idade+1} no proximo aniversário.')
    print(f'Sabemos que você gosta da cor {cor.lower()}!')

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
cor = input('Digite a sua cor favorita: ')
funcao(nome.capitalize(), int(idade), cor)