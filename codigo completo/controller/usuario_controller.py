# controller/usuario_controller.py
from repository.usuario_repository import UsuarioRepository
from config.db_config import db_config
from model.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.repository = UsuarioRepository(db_config)

    def criar_usuario(self, nome, idade, profissao, cidade, genero, email, senha):
        novo_usuario = Usuario(None, nome, idade, profissao, cidade, genero, email, senha)
        self.repository.salvar_usuario(novo_usuario)

    def obter_usuario(self, email):
        return self.repository.obter_usuario_por_email(email)

    def listar_usuarios(self):
        return self.repository.listar_usuarios()
    
    def deletar_usuario(self, usuario_id):
        self.repository.deletar_usuario(usuario_id)

    def fechar_conexao(self):
        self.repository.close_connection()
