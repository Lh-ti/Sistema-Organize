from tkinter import ttk
from typing import Self
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter as messagebox
import psycopg2

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        self.root.geometry(f"{largura_tela}x{altura_tela}-1-1")

        self.tentativas = 0
        self.max_tentativas = 3

        self.create_login_frame()  # Chama o método para criar a interface

    def create_login_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        self.username_label = tk.Label(frame, text="Usuário:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(frame, text="Senha:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = tk.Button(frame, text="Entrar", command=self.check_login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.register_button = tk.Button(frame, text="Cadastrar", command=self.open_registration)
        self.register_button.grid(row=3, columnspan=2, pady=10)

    def check_login(self):
        usuario = self.username_entry.get()
        senha = self.password_entry.get()

        # Validação dos campos
        if not usuario or not senha:
            messagebox.showwarning("Campo Vazio", "Por favor, preencha todos os campos.")
            return

        # Lógica de verificação do usuário e senha
        if usuario == "admin" and senha == "senha123":
            self.on_login()  # Chama a função de login
            self.root.destroy()  # Fecha a tela de login
            new_root = tk.Tk()
            app = TelaPrincipal(new_root)  # Certifique-se de que TelaPrincipal está definida
            new_root.mainloop()
        else:
            self.tentativas += 1  # Incrementa o contador de tentativas
            if self.tentativas >= self.max_tentativas:
                messagebox.showerror("Erro", "Usuário ou senha inválidos!")
                self.root.destroy()  # Fecha a tela de login
            else:
                messagebox.showerror("Erro", f"Usuário ou senha inválidos! Tentativa {self.tentativas} de {self.max_tentativas}.")

            pass    
    def on_login(self):
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

    def open_registration(self):
        # Lógica para abrir tela de cadastro
        self.cadastro = TelaCadastro(self.root)
        self.cadastro.open_registrat
    
    # Método opcional para a funcionalidade de cadastro, pode ser removido se não necessário
    def cadastrar(self):
        # Lógica do botão de cadastro (se necessário)
        print("Abrindo tela de cadastro...")

        pass

class TelaCadastro:
    def __init__(self, root):
        self.root = root

        self.register_window = tk.Toplevel(root)
        self.register_window.title("Cadastro")
        self.register_window.geometry("300x200")
        self.create_registration_form()

    def create_registration_form(self):
        tk.Label(self.register_window, text="Usuário:").pack(pady=10)
        username_entry = tk.Entry(self.register_window)
        username_entry.pack(pady=5)

        tk.Label(self.register_window, text="Senha:").pack(pady=10)
        password_entry = tk.Entry(self.register_window, show="*")
        password_entry.pack(pady=5)

        tk.Button(self.register_window, text="Cadastrar", 
                  command=lambda: self.register_user(username_entry, password_entry)).pack(pady=20)

    def register_user(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Campo Vazio", "Preencha todos os campos.")
        else:
            messagebox.showinfo("Cadastro", f"Usuário {username} cadastrado com sucesso!")

    def register(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        dob = self.dob_entry.get()
        city = self.city_entry.get()
        password = self.password_entry.get()
        accepts_terms = self.terms_var.get()

        if not all([name, age, email, dob, city, password]) or not accepts_terms:
            messagebox.showwarning("Campo Vazio", "Por favor, preencha todos os campos e aceite os termos.")
            return

        # Simula o envio dos dados para um banco de dados
        user_data = {
            "nome": name,
            "idade": age,
            "email": email,
            "data_nascimento": dob,
            "cidade": city,
            "senha": password
        }
        self.users.append(user_data)  # Armazena os dados na lista

        
        messagebox.showinfo("Cadastro", f"Cadastro realizado com sucesso!\nNome: {name}\nIdade: {age}\nEmail: {email}\nData de Nascimento: {dob}\nCidade: {city}")

        # Limpa os campos após o cadastro
        self.clear_fields()

    def clear_fields(self):
         self.name_entry.delete(0, tk.END)
         self.age_entry.delete(0, tk.END)
         self.email_entry.delete(0, tk.END)
         self.dob_entry.delete(0, tk.END)
         self.city_entry.delete(0, tk.END)
         self.password_entry.delete(0, tk.END)
         self.terms_var.set(False)  # Desmarca o checkbox


class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("🟣 Organize")
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        self.root.geometry(f"{largura_tela}x{altura_tela}-1-1")

        # Cores
        self.preto = "#160125"
        self.roxo = "#4B0082"
        self.cinza_claro = "#f7f8fa"
        self.branco = "#ffffff"
        self.cinza_texto = "#7a7a7a"

        self.create_sidebar()
        self.create_main_frame()

    def create_sidebar(self):
        # Frame da barra lateral
        self.sidebar = tk.Frame(self.root, bg=self.roxo, width=250, height=700)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.root.grid_rowconfigure(0, weight=1)

        # Logo 
        logo_frame = tk.Frame(self.sidebar, bg=self.roxo)
        logo_frame.pack(pady=20)
        logo = tk.Label(logo_frame, text="The office", font=("Arial", 20, "bold"), fg=self.branco, bg=self.roxo)
        logo.pack()

        # Botões da barra lateral
        buttons = {
            "Home": self.show_dashboard,
            "Produtos": self.show_products,
            "Estoque": self.show_stock,
            "Caixa": self.show_cashier,
            "Vendedores": self.show_sellers,
            "Usuários": self.show_users
        }
        for text, command in buttons.items():
            self.create_sidebar_button(text, command)

        # Botão "Sair" que fecha a aplicação
        btn_sair = tk.Button(self.sidebar, text="Sair", font=("Arial", 14), bg=self.roxo, fg=self.branco, borderwidth=0, command=self.close_app)
        btn_sair.pack(side="bottom", pady=30)

    def create_sidebar_button(self, text, command):
        button = tk.Button(self.sidebar, text=text, font=("Arial", 14), bg=self.roxo, fg=self.branco, borderwidth=0, anchor="w", command=command)
        button.pack(fill="x", padx=20, pady=10)

    def create_main_frame(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cinza_claro)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.show_dashboard()  # Mostra o Dashboard ao iniciar o programa

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def close_app(self):
        self.root.destroy()

    # Funções para exibir os frames
    def show_dashboard(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Dashboard", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=25)

        self.main_frame.grid_columnconfigure(0, weight=1)

        self.create_sales_graph()
        self.create_categories()
        self.create_stock_numbers()
        self.create_orders_frame()

    def show_products(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Produtos", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=25)

        # Botão "Adicionar Produto" na tela de produtos
        btn_adicionar_produto = tk.Button(self.main_frame, text="Adicionar Produto", font=("Arial", 14), bg=self.roxo, fg=self.branco, command=self.add_product)
        btn_adicionar_produto.grid(row=1, column=0, padx=10, pady=10)

        self.create_product_list()

    def create_product_list(self):
        products_frame = tk.Frame(self.main_frame, bg=self.branco)
        products_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        products = [
            {"name": "Produto 1", "stock": 15, "price": 50.0},
            {"name": "Produto 2", "stock": 10, "price": 30.0},
        ]

        for product in products:
            product_label = tk.Label(products_frame, text=f"{product['name']} - Estoque: {product['stock']} - R$ {product['price']:.2f}", bg=self.branco)
            product_label.pack(padx=10, pady=5)
            
    def add_product(self):
        # Abre a tela de cadastro de produto
        TelaCadastroProduto(self.root, self.show_products)

    def show_stock(self):
        self.clear_main_frame()

        # Título
        title = tk.Label(self.main_frame, text="Estoque", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=3)

        # Pesquisa de Produtos no Estoque com Filtros Avançados
        search_frame = tk.Frame(self.main_frame, bg=self.branco)
        search_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        title = tk.Label(search_frame, text="Pesquisar Produto", font=("Arial", 12), bg=self.branco)
        title.pack(anchor="w", padx=5)

        search_entry = tk.Entry(search_frame, font=("Arial", 12), bg=self.cinza_claro, fg="grey")
        search_entry.pack(anchor="w", padx=5, pady=5)
        search_entry.insert(0, "Digite o nome do produto")

        # Funções para placeholder
        search_entry.bind("<FocusIn>", lambda e: search_entry.delete(0, tk.END) if search_entry.get() == "Digite o nome do produto" else None)
        search_entry.bind("<FocusOut>", lambda e: search_entry.insert(0, "Digite o nome do produto") if search_entry.get() == "" else None)

        # Filtro por categoria
        category_label = tk.Label(search_frame, text="Categoria:", font=("Arial", 12), bg=self.branco)
        category_label.pack(anchor="w", padx=5, pady=5)

        category_combo = ttk.Combobox(search_frame, values=["Todos", "Eletrônicos", "Roupas", "Alimentos"], state="readonly", font=("Arial", 12))
        category_combo.current(0)  # Seleciona a opção "Todos" por padrão
        category_combo.pack(anchor="w", padx=5, pady=5)

        # Filtro por preço
        price_label = tk.Label(search_frame, text="Preço Máximo (R$):", font=("Arial", 12), bg=self.branco)
        price_label.pack(anchor="w", padx=5, pady=5)

        price_entry = tk.Entry(search_frame, font=("Arial", 12), bg=self.cinza_claro)
        price_entry.pack(anchor="w", padx=5, pady=5)

        # Filtro por quantidade
        quantity_label = tk.Label(search_frame, text="Quantidade Mínima:", font=("Arial", 12), bg=self.branco)
        quantity_label.pack(anchor="w", padx=5, pady=5)

        quantity_entry = tk.Entry(search_frame, font=("Arial", 12), bg=self.cinza_claro)
        quantity_entry.pack(anchor="w", padx=5, pady=5)

        # Botão de pesquisa com filtros
        search_button = tk.Button(search_frame, text="Pesquisar", font=("Arial", 12), bg=self.roxo, fg=self.branco, command=self.search_product_with_filters)
        search_button.pack(anchor="w", padx=5, pady=5)

        # Frame para gráficos
        graph_frame = tk.Frame(self.main_frame, bg=self.branco)
        graph_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)

        # Gráfico de estoque (Canvas)
        self.create_stock_chart(graph_frame)

        # Resumo do Estoque Geral
        stock_summary_frame = tk.Frame(self.main_frame, bg=self.branco)
        stock_summary_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        total_items = tk.Label(stock_summary_frame, text="Total de Itens em Estoque: 120", font=("Arial", 14), bg=self.branco)
        total_items.pack(anchor="w", padx=10, pady=5)

        total_value = tk.Label(stock_summary_frame, text="Valor Total do Estoque: R$ 50.000", font=("Arial", 14), bg=self.branco)
        total_value.pack(anchor="w", padx=10, pady=5)

        # Produtos com Estoque Baixo
        low_stock_frame = tk.Frame(self.main_frame, bg=self.branco)
        low_stock_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        title = tk.Label(low_stock_frame, text="Produtos com Estoque Baixo", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        products = [
            {"name": "Produto A", "stock": 2, "replenish": "Pendente"},
            {"name": "Produto B", "stock": 0, "replenish": "Em Andamento"},
        ]
        for product in products:
            product_info = tk.Label(low_stock_frame, text=f"{product['name']}: {product['stock']} unidades (Reabastecimento: {product['replenish']})", bg=self.branco)
            product_info.pack(anchor="w", padx=10)

        # Alertas de Estoque
        alerts_frame = tk.Frame(self.main_frame, bg=self.branco)
        alerts_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
        title = tk.Label(alerts_frame, text="Alertas de Estoque", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        alert = tk.Label(alerts_frame, text="Produto B está esgotado!", font=("Arial", 12), bg=self.branco, fg="red")
        alert.pack(anchor="w", padx=10)


    def create_stock_chart(self, parent_frame):
        """Cria um gráfico simples usando o Canvas."""
        canvas = tk.Canvas(parent_frame, width=300, height=400, bg=self.branco)
        canvas.pack()

        # Exemplo de dados de categorias
        categories = ['Eletrônicos', 'Roupas', 'Alimentos']
        values = [50, 30, 40]  # Quantidade de itens em estoque

        total = sum(values)
        angles = [(value / total) * 360 for value in values]

        # Cores para as categorias
        colors = ['#FF9999', '#99FF99', '#9999FF']

        start_angle = 0
        for i, angle in enumerate(angles):
            # Desenhar uma fatia de pizza para cada categoria
            canvas.create_arc((50, 50, 250, 250), start=start_angle, extent=angle, fill=colors[i])
            start_angle += angle

        # Legenda para o gráfico
        legend_y = 260
        for i, category in enumerate(categories):
            canvas.create_rectangle(10, legend_y, 30, legend_y + 20, fill=colors[i])
            canvas.create_text(50, legend_y + 10, anchor="w", text=f"{category} ({values[i]} itens)", font=("Arial", 12))
            legend_y += 30

    def search_product_with_filters(self):
        """Função para pesquisar produtos usando os filtros aplicados."""
        # search_term = self.search_entry.get()
        # selected_category = self.category_combo.get()
        # max_price = self.price_entry.get()
        # min_quantity = self.quantity_entry.get()


    def show_cashier(self):
        self.clear_main_frame()

        # Título
        title = tk.Label(self.main_frame, text="Caixa", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Campos de Entrada para Produto
        tk.Label(self.main_frame, text="Produto:", font=("Arial", 14), bg=self.cinza_claro).grid(row=1, column=0, padx=10, pady=5)
        self.produto_entry = tk.Entry(self.main_frame, font=("Arial", 12), bg=self.branco)
        self.produto_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Quantidade:", font=("Arial", 14), bg=self.cinza_claro).grid(row=2, column=0, padx=10, pady=5)
        self.quantidade_entry = tk.Entry(self.main_frame, font=("Arial", 12), bg=self.branco)
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Preço Unitário (R$):", font=("Arial", 14), bg=self.cinza_claro).grid(row=3, column=0, padx=10, pady=5)
        self.preco_entry = tk.Entry(self.main_frame, font=("Arial", 12), bg=self.branco)
        self.preco_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botão Adicionar ao Carrinho
        add_button = tk.Button(self.main_frame, text="Adicionar ao Carrinho", font=("Arial", 14), bg=self.roxo, fg=self.branco, command=self.add_to_cart)
        add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Exibição da Lista de Produtos
        self.tree = ttk.Treeview(self.main_frame, columns=("Produto", "Quantidade", "Preço Total"), show="headings")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Preço Total", text="Preço Total (R$)")
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Rótulo de Total
        self.total_label = tk.Label(self.main_frame, text="Total: R$ 0.00", font=("Arial", 14), bg=self.cinza_claro)
        self.total_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        tk.Label(self.main_frame, text="Forma de Pagamento:", font=("Arial", 14), bg=self.cinza_claro).grid(row=7, column=0, padx=10, pady=5)
        self.payment_method = tk.StringVar(value="Dinheiro")
        payment_options = ttk.Combobox(self.main_frame, textvariable=self.payment_method, values=["Dinheiro", "Pix", "Cartão de Crédito", "Cartão de Débito"], state="readonly")
        payment_options.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Valor Pago (R$):", font=("Arial", 14), bg=self.cinza_claro).grid(row=8, column=0, padx=10, pady=5)
        self.payment_entry = tk.Entry(self.main_frame, font=("Arial", 12), bg=self.branco)
        self.payment_entry.grid(row=8, column=1, padx=10, pady=5)

        # Botão Finalizar Compra
        finalize_button = tk.Button(self.main_frame, text="Finalizar Compra", font=("Arial", 14), bg=self.roxo, fg=self.branco, command=self.finalize_purchase)
        finalize_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Rótulo de Troco
        self.change_label = tk.Label(self.main_frame, text="", font=("Arial", 14), bg=self.cinza_claro)
        self.change_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

    # Método Adicionar ao Carrinho
    def add_to_cart(self):
        produto = self.produto_entry.get()
        quantidade = int(self.quantidade_entry.get())
        preco_unitario = float(self.preco_entry.get())
        preco_total = quantidade * preco_unitario

        # Adiciona item ao Treeview
        self.tree.insert("", "end", values=(produto, quantidade, f"R$ {preco_total:.2f}"))

        # Atualiza o total
        self.total_value = getattr(self, 'total_value', 0) + preco_total
        self.total_label.config(text=f"Total: R$ {self.total_value:.2f}")

        # Limpa as entradas
        self.produto_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)

        # Método Finalizar Compra
    def finalize_purchase(self):
        payment_method = self.payment_method.get()
        payment = float(self.payment_entry.get())
        total = self.total_value

        if payment < total and payment_method == "Dinheiro":
            self.change_label.config(text="Valor insuficiente!", fg="red")
        else:
            change = payment - total
            self.change_label.config(text=f"Troco: R$ {change:.2f}", fg="green")

            # Gera Nota Fiscal
            self.show_receipt()

            # Limpa o carrinho e reseta
            self.tree.delete(*self.tree.get_children())
            self.total_value = 0
            self.total_label.config(text="Total: R$ 0.00")
            self.payment_entry.delete(0, tk.END)

    def show_receipt(self):
        receipt_window = tk.Toplevel(self.main_frame)
        receipt_window.title("Nota Fiscal")
        
        # Texto da Nota Fiscal
        receipt_text = tk.Text(receipt_window, width=50, height=15)
        receipt_text.pack(pady=10)

        # Monta a Nota Fiscal
        receipt = "--------------Nota Fiscal--------------\n"
        receipt += "-" * 40 + "\n"
        for child in self.tree.get_children():
            item = self.tree.item(child)["values"]
            receipt += f"Produto: {item[0]}  X {item[1]}  Preço:{item[2]}\n"
        receipt += "-" * 40 + "\n"
        receipt += f"Total: R$ {self.total_value:.2f}\n"
        receipt += f"Forma de Pagamento: {self.payment_method.get()}\n"
        receipt += "-" * 40 + "\n"

        receipt_text.insert(tk.END, receipt)
        receipt_text.config(state=tk.DISABLED)  # Torna o texto somente leitura

        # Botão "Imprimir" a nota fiscal
        print_button = tk.Button(receipt_window, text="Imprimir", command=lambda: self.print_receipt(receipt))
        print_button.pack(pady=10)

    def show_sellers(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Vendedores", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.create_sellers_list()

    def show_users(self):  # Nova função para mostrar usuários
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Usuários Cadastrados", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Frame para a lista de usuários
        user_list_frame = tk.Frame(self.main_frame, bg=self.branco)
        user_list_frame.grid(row=1, column=0, padx=10, pady=10)

        # Exibir a tabela de usuários
        self.create_user_table(user_list_frame)

    def create_user_table(self, parent):  # Método para criar a tabela de usuários
        columns = ("id", "nome", "idade", "profissao", "cidade", "genero", "email")
        self.user_tree = ttk.Treeview(parent, columns=columns, show="headings")
        
        # Definindo cabeçalhos
        for col in columns:
            self.user_tree.heading(col, text=col.capitalize())
            self.user_tree.column(col, anchor="w")

        self.user_tree.pack(fill="both", expand=True)

        # Exemplo de dados de usuários
        users = [
            (1, "João Silva", 30, "Desenvolvedor", "São Paulo", "Masculino", "joao@example.com"),
            (2, "Maria Souza", 25, "Designer", "Rio de Janeiro", "Feminino", "maria@example.com"),
            (3, "Carlos Pereira", 35, "Gerente", "Belo Horizonte", "Masculino", "carlos@example.com"),
        ]

        # Adicionando os dados à tabela
        for user in users:
            self.user_tree.insert("", "end", values=user)

    def exit_application(self):
        self.root.destroy()

    # Componentes do Dashboard
    def create_sales_graph(self):
        grafico_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        grafico_frame.grid(row=1, column=0, padx=10, pady=10)
        title = tk.Label(grafico_frame, text="Vendas", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Exemplo de dados de vendas
        meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
        vendas = [100, 200, 150, 300, 250]

         # Gráfico de linha
        ax.plot(meses, vendas, marker='o', color=self.roxo)
        ax.set_title('Vendas Mensais')
        ax.set_xlabel('Mês')
        ax.set_ylabel('Quantidade Vendida')

        # Gráfico ao tkinter através do FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=grafico_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def create_categories(self):
        categorias_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        categorias_frame.grid(row=1, column=1, padx=10, pady=10)
        title = tk.Label(categorias_frame, text="Categorias de itens principais", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        categories_placeholder = tk.Label(categorias_frame, text="Categorias de itens", bg=self.branco, width=40, height=25)
        categories_placeholder.pack(padx=10, pady=10)

    def create_stock_numbers(self):
        numeros_estoque_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        numeros_estoque_frame.grid(row=1, column=2, padx=10, pady=10)
        title = tk.Label(numeros_estoque_frame, text="Números do Estoque", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        stock_numbers_placeholder = tk.Label(numeros_estoque_frame, text="Total de itens e valor", bg=self.branco, width=50, height=25)
        stock_numbers_placeholder.pack(padx=10, pady=10)

    def create_orders_frame(self):
        pedidos_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        pedidos_frame.grid(row=1, column=3, padx=10, pady=10)
        title = tk.Label(pedidos_frame, text="Pedidos", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        orders_placeholder = tk.Label(pedidos_frame, text="Lista de pedidos", bg=self.branco, width=40, height=8)
        orders_placeholder.pack(padx=10, pady=10)


    def create_orders_frame(self):
        pedidos_frame = tk.Frame(self.main_frame, bg=self.branco, width=50, height=50)
        pedidos_frame.grid(row=2, column=0, columnspan=125, padx=25, pady=70)
        pedido_labels = ["REEMBOLSOS", "MENSAGEM", "NOVOS ITENS", "NOVAS ORDENS", "ITENS FALTANDO"]
        pedido_values = ["12", "1", "67", "190", "11"]

        for i in range(5):
            pedido_frame = tk.Frame(pedidos_frame, bg=self.branco)
            pedido_frame.grid(row=0, column=i, padx=20)
            pedido_num = tk.Label(pedido_frame, text=pedido_values[i], font=("Arial", 24), bg=self.branco, fg=self.roxo)
            pedido_num.pack()
            pedido_texto = tk.Label(pedido_frame, text=pedido_labels[i], font=("Arial", 12), bg=self.branco, fg=self.cinza_texto)
            pedido_texto.pack()
        
    def create_product_list(self):
        products_frame = tk.Frame(self.main_frame, bg=self.branco)
        products_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        # Lista de produtos
        products = [
            {"name": "Produto 1", "stock": 15, "price": 50.0, "image": "placeholder.png"},
            {"name": "Produto 2", "stock": 10, "price": 30.0, "image": "placeholder.png"},
            {"name": "Produto 3", "stock": 5, "price": 45.0, "image": "placeholder.png"},
            {"name": "Produto 4", "stock": 8, "price": 60.0, "image": "placeholder.png"},
            {"name": "Produto 5", "stock": 12, "price": 20.0, "image": "placeholder.png"},
            {"name": "Produto 6", "stock": 7, "price": 35.0, "image": "placeholder.png"},
            {"name": "Produto 7", "stock": 3, "price": 15.0, "image": "placeholder.png"},
            {"name": "Produto 8", "stock": 9, "price": 70.0, "image": "placeholder.png"},
        ]

        # Grid com 4 por linha e 2 por coluna
        max_columns = 4  # Máximo de 4 produtos por linha
        row = 0
        col = 0

        for index, product in enumerate(products):
            product_frame = tk.Frame(products_frame, bg=self.branco, bd=2, relief="solid", padx=10, pady=10)
            product_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Placeholder para imagem do produto
            image = tk.Label(product_frame, text="📦", bg=self.branco, width=10, height=5)
            image.grid(row=0, column=0, padx=10, pady=10)

            # Nome do produto
            name_label = tk.Label(product_frame, text=product["name"], font=("Arial", 14), bg=self.branco)
            name_label.grid(row=1, column=0, padx=10)

            # Estoque e preço
            stock_price_label = tk.Label(product_frame, text=f"Estoque: {product['stock']} - R$ {product['price']:.2f}", bg=self.branco)
            stock_price_label.grid(row=2, column=0, padx=10)

            # Botão para mais informações
            btn_info = tk.Button(product_frame, text="Mais Informações", bg=self.roxo, fg=self.branco)
            btn_info.grid(row=3, column=0, padx=10)

            # Botão para adicionar ao carrinho
            btn_add_cart = tk.Button(product_frame, text="Adicionar ao Carrinho", bg=self.roxo, fg=self.branco)
            btn_add_cart.grid(row=4, column=0, padx=10)

            # Controle de colunas e linhas
            col += 1
            if col == max_columns:
                col = 0
                row += 1

    # Componentes da lista de Vendedores
    def create_sellers_list(self):
        # Ajustando a largura do sellers_frame
        sellers_frame = tk.Frame(self.main_frame, bg=self.cinza_claro, width=700)
        sellers_frame.grid(row=1, column=0, padx=200, pady=10, sticky="nsew")
        
        sellers = [
            {"name": "Vendedor 1", "id": "001"},
            {"name": "Vendedor 2", "id": "002"},
            {"name": "Vendedor 3", "id": "003"},
        ]

        for seller in sellers:
            # Card para cada vendedor
            seller_frame = tk.Frame(sellers_frame, bg=self.branco, bd=2, relief="groove", padx=20, pady=10)
            seller_frame.pack(padx=10, pady=10, fill="x")

            name_label = tk.Label(seller_frame, text=seller["name"], font=("Arial", 16, "bold"), bg=self.branco, fg=self.roxo)
            name_label.grid(row=0, column=0, padx=10, sticky="w")

            id_label = tk.Label(seller_frame, text=f"ID: {seller['id']}", font=("Arial", 12), bg=self.branco, fg=self.cinza_texto)
            id_label.grid(row=1, column=0, padx=10, sticky="w")

            label = tk.Button(seller_frame, text="|", bg="white", fg="white", borderwidth=0)
            label.grid(row=0, column=1, padx=200, sticky="e")

            btn_editar = tk.Button(seller_frame, text="📝", bg=self.cinza_claro, fg="blue", borderwidth=0, font=("Arial", 12))
            btn_editar.grid(row=0, column=1, padx=10, sticky="e")

            btn_delete = tk.Button(seller_frame, text="🗑️", bg="red", fg=self.branco, borderwidth=0, font=("Arial", 12))
            btn_delete.grid(row=0, column=2, padx=10, sticky="e")
    
class TelaCadastroProduto:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.create_form()

    def create_form(self):
        self.window = tk.Toplevel(self.master)
        self.window.title("Adicionar Produto")
        self.window.geometry("300x250")

        tk.Label(self.window, text="Nome do Produto:").pack(pady=5)
        self.nome_entry = tk.Entry(self.window)
        self.nome_entry.pack(pady=5)

        tk.Label(self.window, text="Quantidade em estoque:").pack(pady=5)
        self.qnt_entry = tk.Entry(self.window)
        self.qnt_entry.pack(pady=5)

        tk.Label(self.window, text="Preço:").pack(pady=5)
        self.preco_entry = tk.Entry(self.window)
        self.preco_entry.pack(pady=5)

        tk.Button(self.window, text="Adicionar", command=self.add_product).pack(pady=20)

    def add_product(self):
        nome = self.nome_entry.get()
        qnt = self.qnt_entry.get()
        preco = self.preco_entry.get()

        # Aqui você pode adicionar a lógica para salvar o produto
        if nome and qnt and preco:
            messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")
            self.window.destroy()  # Fecha a janela após adicionar o produto
            self.callback()  # Atualiza a tela de produtos
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipal(root)
    root.mainloop()
