from random import randrange as r
from time import time as t

num_perguntas = int(input('Quantas perguntas você gostaria?: '))
max_num = int(input('Qual maior número gostaria de práticar?: '))

pontos = 0
lista_respostas = []

comeco = t()
for q in range(num_perguntas):
    num1, num2 = r(1,max_num+1),r(1,max_num+1)
    questao = num1 * num2
    resposta = int(input(f'{num1} X {num2} = '))
    lista_respostas.append(f'{num1} X {num2} = {questao}. Você {resposta}')
    if questao == resposta:
        pontos += 1
    fim = t()

print(f'Obrigado por jogar! \nVocê teve uma pontuação de {pontos} em {num_perguntas} perguntas. Precisão: {round(pontos/num_perguntas*100)}% em {round((fim-comeco)/num_perguntas,1)} segundos por pergunta.')
for i in lista_respostas:
    print(i)