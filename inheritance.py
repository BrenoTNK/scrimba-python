class Pessoa:
    # Classe abstrata pessoa;
    def andar(self):
        print('Andar 4 passos')
    def descançar(self):
        print('Ganhar 4 pontos de vida')

class Doutor(Pessoa):
    # Classe filha de pessoa;
    def curar(self):
        print('Recuperar 10 pontos de vida')

class Lutador(Pessoa):
    # Classe filha de pessoa;
    def lutar(self):
        print('Dano de 10 pontos de vida')
    def andar(self):
        print('Andar 6 passos')

class Mago(Doutor, Lutador):
    # Classe filha de lutador e doutor;
    def cajado(self):
        print('Ficar invisivel')
    def curar(self):
        print('Curar 15 pontos de vida')

    # Objeto = class()
personagem1 = Mago()

    # Objeto.Ação()
personagem1.curar()