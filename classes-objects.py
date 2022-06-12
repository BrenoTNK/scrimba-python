class Filme:
    def __init__(self, titulo, ano, imdb, assistiu):
        self.titulo = titulo
        self.ano = ano
        self.imdb = imdb
        self.assistiu = assistiu
    
    def mostrar(self):
        print('Titulo: ', self.titulo)
        print('Ano de produção: ', self.ano)
        print('IMDB: ', self.imdb)
        print('Já assistiu? ', self.assistiu)

filme_1 = Filme('Life of Brian', 1979, 8.1, True)
filme_2 = Filme('The Holy Grail', 1975, 8.2, False)

#print(filme_1.titulo, filme_1.imdb)

#filme_2.mostrar()
#Filme.mostrar(filme_2)

filmes = [filme_1, filme_2]
print(filmes[1].titulo, filmes[0].titulo)
filmes[0].mostrar()