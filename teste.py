import tkinter as tk
from tkinter import font

class TelaInicial:
    def __init__(self, master):
        self.master = master
        self.master.title("Organize - Sistema de Vendas")
        self.master.geometry("500x300")
        self.master.configure(bg="black")

        # Definir a fonte do título
        titulo_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Adicionar o título
        self.titulo = tk.Label(self.master, text="Organize", bg="black", fg="white", font=titulo_font)
        self.titulo.pack(pady=20)

        # Personalizar botões
        button_font = font.Font(family="Arial", size=14, weight="bold")  # Definir fonte personalizada

        # Botão de Administrador
        self.btn_administrador = tk.Button(
            self.master, 
            text="Administrador", 
            width=15, 
            height=2,  # Altura do botão
            bg="gray",  # Cor de fundo
            fg="white",  # Cor do texto
            font=button_font,  # Fonte
            relief="raised",  # Borda elevada
            bd=5,  # Espessura da borda
            command=self.abrir_login_administrador  # Função chamada ao clicar
        )
        self.btn_administrador.pack(pady=10)

        # Botão de Vendedor
        self.btn_vendedor = tk.Button(
            self.master, 
            text="Vendedor", 
            width=15, 
            height=2, 
            bg="green",  # Cor de fundo
            fg="white",  # Cor do texto
            font=button_font, 
            relief="sunken",  # Borda afundada
            bd=5,  # Espessura da borda
            command=self.vendedor
        )
        self.btn_vendedor.pack(pady=10)

        # Botão de Criar Conta
        self.btn_criar_conta = tk.Button(
            self.master, 
            text="Criar Conta", 
            width=15, 
            height=2, 
            bg="purple",  # Cor de fundo
            fg="white",  # Cor do texto
            font=button_font, 
            relief="solid",  # Borda sólida
            bd=5,  # Espessura da borda
            command=self.criar_conta
        )
        self.btn_criar_conta.pack(pady=10)

    # Função para abrir a tela de login do Administrador
    def abrir_login_administrador(self):
        login_janela = tk.Toplevel(self.master)
        login_janela.title("Login - Administrador")
        login_janela.geometry("400x200")
        login_janela.configure(bg="black")
        
        # Adicionar título da tela de login
        login_titulo = tk.Label(login_janela, text="Login Administrador", bg="black", fg="white", font=("Helvetica", 18, "bold"))
        login_titulo.pack(pady=20)

        # Criar campos de login
        lbl_usuario = tk.Label(login_janela, text="Usuário:", bg="black", fg="white")
        lbl_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(login_janela, width=30)
        self.entry_usuario.pack(pady=5)

        lbl_senha = tk.Label(login_janela, text="Senha:", bg="black", fg="white")
        lbl_senha.pack(pady=5)
        self.entry_senha = tk.Entry(login_janela, show="*", width=30)
        self.entry_senha.pack(pady=5)

        btn_login = tk.Button(login_janela, text="Entrar", command=self.verificar_login)
        btn_login.pack(pady=20)

    # Funções adicionais
    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == "admin" and senha == "1234":
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha inválidos.")

    def vendedor(self):
        print("Vendedor selecionado")

    def criar_conta(self):
        print("Criar Conta selecionado")

# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
