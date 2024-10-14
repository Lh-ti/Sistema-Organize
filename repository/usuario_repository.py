import psycopg2
from psycopg2 import sql
from model.usuario import Usuario

class UsuarioRepository:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def salvar_usuario(self, usuario):
        with self.connection.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO usuarios (nome, idade, profissao, cidade, genero, email, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (usuario.nome, usuario.idade, usuario.profissao,
                                           usuario.cidade, usuario.genero, usuario.email,
                                           usuario.senha))
            self.connection.commit()

    def obter_usuario_por_email(self, email):
        with self.connection.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id, nome, idade, profissao, cidade, genero, email, senha
                FROM usuarios
                WHERE email = %s
            """)
            cursor.execute(select_query, (email,))
            result = cursor.fetchone()
            if result:
                return Usuario(*result)
            return None

    def listar_usuarios(self):
        usuarios = []
        with self.connection.cursor() as cursor:
            select_query = sql.SQL("SELECT * FROM usuarios")
            cursor.execute(select_query)
            for row in cursor.fetchall():
                usuarios.append(Usuario(*row))
        return usuarios

    def deletar_usuario(self, usuario_id):
        with self.connection.cursor() as cursor:
            delete_query = sql.SQL("DELETE FROM usuarios WHERE id = %s")
            cursor.execute(delete_query, (usuario_id,))
            self.connection.commit()
