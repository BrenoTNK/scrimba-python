nome = input('Digite seu nome: ')
km = input('Digite a distancia em kilometros: ')

mi = float(km)/1.609

print(f'Olá {nome.title()}! {km}km é igual a {round(mi, 1)} milias.')