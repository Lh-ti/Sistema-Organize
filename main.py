import tkinter as tk
from view.usuario_view import UsuarioView
from controller.usuario_controller import UsuarioController
from tkinter import messagebox
from view.dashboard_view import TelaPrincipal
from view.dashboard_view import TelaLogin
import psycopg2
import tkinter as tk
from tkinter import messagebox

def conectar_banco():
    conn = psycopg2.connect(
        dbname='senac',
        user='postgres',
        password='postgres',
        host='localhost'
    )
    return conn


def realizar_login_callback():
    email = usuario_view.entry_usuario.get()
    senha = usuario_view.entry_senha.get()
    
    conn = conectar_banco()
    cursor = conn.cursor()

    # Verifica se as credenciais estão corretas
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
    usuario = cursor.fetchone()
    
    if usuario:
        print("Login bem-sucedido!")
        usuario_view.master.destroy()  # Fecha a janela de login
        root = tk.Tk()  # Abre uma nova janela
        app = TelaPrincipal(root)  # Abre o dashboard
        app = TelaLogin(root)
        root.mainloop()
    else:
        messagebox.showerror("Erro", "Email ou senha incorretos.")

    cursor.close()
    conn.close()

def main():
    global usuario_view  # Tornar global para ser acessível no callback
    global usuario_controller  # Torna usuario_controller global

    root = tk.Tk()
    usuario_controller = UsuarioController()
    usuario_view = UsuarioView(root, usuario_controller)
    usuario_view.mostrar_tela_login(realizar_login_callback, usuario_view.mostrar_formulario_cadastro)

    root.mainloop()
    usuario_controller.fechar_conexao()

if __name__ == "__main__":
    main()