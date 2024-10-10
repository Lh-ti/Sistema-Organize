
import tkinter as tk
from view.usuario_view import UsuarioView
from controller.usuario_controller import UsuarioController
from tkinter import messagebox
from dashboard_view import TelaPrincipal

def realizar_login_callback():
    email = usuario_view.entry_usuario.get()
    senha = usuario_view.entry_senha.get()
    if email == 'leo@gmail.com' and senha == '123456':
        print("Login bem-sucedido!")
        usuario_view.master.destroy()  # Certifique-se de que o root é atribuído corretamente
        root = tk.Tk()  # Abre uma nova janela
        app = TelaPrincipal(root)  # Abre o dashboard
        root.mainloop()
    else:
        messagebox.showerror("Erro", "Email ou senha incorretos.")

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
