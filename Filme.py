class Filme:
    def __init__(self, titulo, genero, ano, codigo, disponivel=True):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.codigo = codigo
        self.disponivel = disponivel