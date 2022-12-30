class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._likes} Likes"

###########################################################################

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao}min - {self._likes} Likes"

###########################################################################

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes"

###########################################################################

#class Playlist(list):
#   def __init__(self, nome, programas):
#       self.nome = nome
#       super().__init__(programas)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
#Duck_type = faz a classe se comportar como um interavel
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

#magic metodo
    def __len__(self):
        return len(self._programas)










