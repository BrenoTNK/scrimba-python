'''
   Simplificando um código do número de dias em um
   determinado mês;
'''

def num_dia(mes):
    dia = 31
    if mes in {'abr', 'jun', 'set', 'nov'}:
        dia = 30
    elif mes == 'fev':
        dia = 28
    print(f'O número de dias no mês de {mes} é {dia}' )

num_dia('jul')
