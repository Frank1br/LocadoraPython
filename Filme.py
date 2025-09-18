class Filme:
    def __init__(self, titulo, genero, ano, codigo, disponivel=True):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.disponivel = True