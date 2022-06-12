nomes = ['john ClEEse', 'Eric IDLE', 'michael']
nomes1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'Você está convidado para a festa este sábado!'

nomes += (nomes1)
for i in range(2):
    nomes.append(input('Digite um novo nome: '))

for nome in nomes:
    msg1 = f'{nome.title()}! {msg}'
    print(msg1)