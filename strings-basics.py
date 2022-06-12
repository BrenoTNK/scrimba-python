msg = 'python é muito bom!'

print(msg.upper())      # Tudo em caixa alta;
print(msg.lower())      # Tudo em caixa baixa;
print(msg.capitalize()) # Primeiro caracter da frase em maiúsculo;
print(msg.title())      # Todas as palavras com a primeira letra em maiúsculo;

print(len(msg))         # Conta quantos caracteres tem;
print(msg.count('o'))   # Conta a quantidade de 'o' que existe na frase;

print(msg[0])           # Mostra o primeiro caracter (começa em 0);
print(msg[-1])          # Mostra o ultimo caracter;
print(msg[2:10])        # Mostra os caracteres de uma posição até a anterior outra (nesse caso 9);

print(msg.find('h'))    # Mostra a posição do 1° carater 'h';
print(msg.find('bom'))  # Aqui é a posição onde começa a palavra;

print(msg.replace('python', 'javascript'))      # Troca a palavra por outra;

print('python' in msg)      # Se existe a palavra;
print('python' not in msg)  # Se não existe a palavra;


nome = 'JOAQUIM'
cor = 'AZUL'

    # As strings vão aparecer como foram definidas nas variaveis;
msg1 = '[' + nome + '] gosta da cor ' + cor + '!'

    # Formatando as strings usando o f'';
msg2 = f'[{nome.capitalize()}] gosta da cor {cor.lower()}!'

print(msg1)
print(msg2)