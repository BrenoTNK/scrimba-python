'''
Lambda equivalente a:

def f(x):
    return x + 5 
'''
f = lambda x : x + 5
print(f(2))


'''
def espaco(str):
   return ''.join(str.split(' '))
'''
espaco = lambda str : ''.join(str.split(' '))
print(espaco('Monty Python Flying Circus'))


'''
def juntar_listas_sem_repeticao(lista_a,lista_b):
   return list(set(lista_a + lista_b))
lista_a = [1,2,3,4]
lista_b = [3,4,5,6,7]
'''
lista_a = [1,2,3,4]
lista_b = [3,4,5,6,7]
juntar_listas_sem_repeticao = lambda lista_a,lista_b:list(set(lista_a + lista_b))
print(juntar_listas_sem_repeticao(lista_a,lista_b))


def criar_quad_func(a,b,c):
    return lambda x : a*x**2 + b*x + c
f = criar_quad_func(2,4,6)
g = criar_quad_func(1,2,3)
print(f(2))
print(g(2))


cancoes = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(cancoes))
print(sorted(cancoes, key = lambda id : int(id[3:])))



class Jogador:
   def __init__(self, nome, pontuacao):
       self.nome = nome
       self.pontuacao =  pontuacao

Eric = Jogador('Eric', 116700)
John = Jogador('John', 24327)
Terry = Jogador('Terry', 150000)
jogadores_lista = [Eric, John, Terry]

jogadores_lista.sort(key = lambda player : player.pontuacao, reverse = True)
print([jogador.nome for jogador in jogadores_lista])
