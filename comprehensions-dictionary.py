filmes = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
anos =[1971,1975,1979,1982,1983,2014]
nomes = ['John','Eric','Michael','Graham','Terry','TerryG']
print(list(zip(filmes, anos)))

    # Codigo 1;
novo_dicio = dict()
for filme, yr in zip(filmes,anos):
    novo_dicio[filme] = yr
print(novo_dicio)
    # Equivalente;                                      Colocada um condição como exemplo
novo_dicio = {filme:yr for filme,yr in zip(filmes,anos) if yr < 1983 and filme.startswith('Monty')}
print(novo_dicio)


n1 = [(nome,filme,yr) for nome,filme,yr in zip(nomes,filmes,anos) if yr < 1981]
print(n1)