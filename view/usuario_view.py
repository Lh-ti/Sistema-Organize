import tkinter as tk
from tkinter import messagebox

class UsuarioView:
    def __init__(self, master, usuario_controller):
        self.master = master
        self.usuario_controller = usuario_controller
        self.master.title("Tela de Login")
        self.master.geometry("400x400")

        self.entry_usuario = None
        self.entry_senha = None
        
    def mostrar_tela_login(self, realizar_login_callback, abrir_formulario_cadastro_callback):
        self.master.deiconify()  # Mostra a tela de login

        label_login = tk.Label(self.master, text="🔐 Login", font=("Arial", 16, "bold"))
        label_login.pack(pady=10)

        # Frame para os campos de login
        frame_login = tk.Frame(self.master, bd=2, relief="solid", padx=10, pady=10)
        frame_login.pack(pady=20, padx=20)

        tk.Label(frame_login, text="Email:", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(2, 2), sticky='w')
        self.entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
        self.entry_usuario.grid(row=1, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_login, text="Senha:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(2, 2), sticky='w')
        self.entry_senha = tk.Entry(frame_login, show='*', font=("Arial", 12))
        self.entry_senha.grid(row=3, column=0, padx=5, pady=(2, 10))

        botao_login = tk.Button(frame_login, text="Login", command=realizar_login_callback, font=("Arial", 12))
        botao_login.grid(row=4, columnspan=2, pady=10)

        botao_cadastro = tk.Button(frame_login, text="Criar Conta", command=abrir_formulario_cadastro_callback, font=("Arial", 12))
        botao_cadastro.grid(row=5, columnspan=2, pady=10)

    def mostrar_formulario_cadastro(self):
        self.master.withdraw()  # Esconde a janela de login
        self.tela_cadastro = tk.Toplevel(self.master)
        self.tela_cadastro.title("Criar Nova Conta")
        self.tela_cadastro.geometry("400x600")

        label_cadastro = tk.Label(self.tela_cadastro, text="📝 Criar Nova Conta", font=("Arial", 16, "bold"))
        label_cadastro.pack(pady=10)

        # Frame para os campos de cadastro
        frame_cadastro = tk.Frame(self.tela_cadastro, bd=2, relief="solid", padx=10, pady=10)
        frame_cadastro.pack(pady=20, padx=20)

        # Campos do formulário
        tk.Label(frame_cadastro, text="Nome:", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_nome = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_nome.grid(row=1, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Idade:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_idade = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_idade.grid(row=3, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Profissão:", font=("Arial", 13, "bold")).grid(row=4, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_profissao = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_profissao.grid(row=5, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Cidade:", font=("Arial", 13, "bold")).grid(row=6, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_cidade = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_cidade.grid(row=7, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Gênero:", font=("Arial", 13, "bold")).grid(row=8, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_genero = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_genero.grid(row=9, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Email:", font=("Arial", 13, "bold")).grid(row=10, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_email = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_email.grid(row=11, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Senha:", font=("Arial", 13, "bold")).grid(row=12, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_senha = tk.Entry(frame_cadastro, show='*', font=("Arial", 12))
        entry_senha.grid(row=13, column=0, padx=5, pady=(2, 10))

        # Botão para salvar usuário
        botao_salvar = tk.Button(frame_cadastro, text="Salvar", command=lambda: self.salvar_usuario(
            entry_nome.get(),
            entry_idade.get(),
            entry_profissao.get(),
            entry_cidade.get(),
            entry_genero.get(),
            entry_email.get(),
            entry_senha.get()
        ), font=("Arial", 12))
        botao_salvar.grid(row=16, columnspan=2, pady=10)

    def salvar_usuario(self, nome, idade, profissao, cidade, genero, email, senha):
        self.usuario_controller.criar_usuario(nome, idade, profissao, cidade, genero, email, senha)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.tela_cadastro.destroy()  # Fecha a tela de cadastro
        self.master.deiconify()  # Mostra a tela de login novamente
