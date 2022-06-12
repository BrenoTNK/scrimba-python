import random

bolsa = ('verde', 'verde', 'verde', 'verde', 'verde', 'preta', 'vermelho', 'vermelho', 'vermelho', 'branca')

bolada_inicial = 1000
bolada = bolada_inicial
resultado = 0
rounds = 3
bolinha = None

print(f'Você começa o jogo com {bolada_inicial} moedas.')

for i in range(1, rounds+1):
    aposta = int(input(f'Atual bolada: {bolada}. Última bolinha {bolinha} \nRound {i} - Quanto vai ser sua aposta?: '))

    bolinha = random.choice(bolsa)

    if bolinha == 'verde':
        resultado = aposta
    elif bolinha == 'preta':
        resultado = 10 * aposta
    elif bolinha == 'branca':
        resultado == -5 * aposta
    else:
        resultado = -aposta
    
    bolada += resultado

    if bolada < 0.5 * bolada_inicial:
        print(f'Fim de jogo! Você perdeu muitas moedas!!!')
        break

    print(f'Bolada: {bolada}, último resultado: ({bolinha}) : ({resultado})')
    print('')

print('Boalda inicial / final: ', bolada_inicial, '/',bolada)
print('Ganhos / perdas: ', ((bolada-bolada_inicial)/bolada_inicial *100),'%')