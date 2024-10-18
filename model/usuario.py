class Usuario:
    def __init__(self, id: int, nome: str, idade: int, profissao: str, cidade: str, genero: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade
        self.genero = genero
        self.email = email
        self.senha = senha
