import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de vendas")
        self.root.geometry("1200x700")

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
        self.sidebar = tk.Frame(self.root, bg=self.preto, width=250, height=700)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Logo
        logo_frame = tk.Frame(self.sidebar, bg=self.preto)
        logo_frame.pack(pady=20)
        logo = tk.Label(logo_frame, text="Organize", font=("Arial", 20, "bold"), fg=self.branco, bg=self.preto)
        logo.pack()

        # Botões da barra lateral
        buttons = {
            "Home": self.show_dashboard,
            "Produtos": self.show_products,
            "Estoque": self.show_stock,
            "Caixa": self.show_cashier,
            "Vendedores": self.show_sellers,
        }
        for text, command in buttons.items():
            self.create_sidebar_button(text, command)

        # Botão "Adicionar produto" e "Sair"
        btn_adicionar = tk.Button(self.sidebar, text="+ Adicionar produto", font=("Arial", 14), bg=self.branco, fg=self.roxo, borderwidth=0)
        btn_adicionar.pack(pady=30)

        btn_sair = tk.Button(self.sidebar, text="Sair", font=("Arial", 14), bg=self.preto, fg=self.branco, borderwidth=0, command=self.exit_application)
        btn_sair.pack(side="bottom", pady=30)

    def create_sidebar_button(self, text, command):
        button = tk.Button(self.sidebar, text=text, font=("Arial", 14), bg=self.preto, fg=self.branco, borderwidth=0, anchor="w", command=command)
        button.pack(fill="x", padx=20, pady=10)

    def create_main_frame(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cinza_claro)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.show_dashboard()  # Mostra o Dashboard ao iniciar o programa

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Exibir os frames
    def show_dashboard(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Dashboard", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.create_sales_graph()
        self.create_categories()
        self.create_stock_numbers()
        self.create_orders_frame()

    def show_products(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Produtos", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.create_product_list()

    def show_stock(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Estoque", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Resumo do Estoque Geral
        stock_summary_frame = tk.Frame(self.main_frame, bg=self.branco)
        stock_summary_frame.grid(row=1, column=0, padx=10, pady=10)
        total_items = tk.Label(stock_summary_frame, text="Total de Itens em Estoque: 120", font=("Arial", 14), bg=self.branco)
        total_items.pack(anchor="w", padx=10, pady=5)
        total_value = tk.Label(stock_summary_frame, text="Valor Total do Estoque: R$ 50.000", font=("Arial", 14), bg=self.branco)
        total_value.pack(anchor="w", padx=10, pady=5)

        # Produtos com Estoque Baixo
        low_stock_frame = tk.Frame(self.main_frame, bg=self.branco)
        low_stock_frame.grid(row=1, column=3, padx=10, pady=10)
        title = tk.Label(low_stock_frame, text="Produtos com Estoque Baixo", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        products = [
            {"name": "Produto A", "stock": 2, "replenish": "Pendente"},
            {"name": "Produto B", "stock": 0, "replenish": "Em Andamento"},
        ]
        for product in products:
            product_info = tk.Label(low_stock_frame, text=f"{product['name']}: {product['stock']} unidades (Reabastecimento: {product['replenish']})", bg=self.branco)
            product_info.pack(anchor="w", padx=10)

        # Histórico de Movimentação de Estoque
        history_frame = tk.Frame(self.main_frame, bg=self.branco)
        history_frame.grid(row=4, column=3, padx=10, pady=10)
        title = tk.Label(history_frame, text="Histórico de Movimentação de Estoque", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        history = [
            {"date": "10/10/2024", "product": "Produto A", "qty": 5, "reason": "Venda"},
            {"date": "09/10/2024", "product": "Produto B", "qty": 10, "reason": "Reabastecimento"},
        ]
        for entry in history:
            entry_info = tk.Label(history_frame, text=f"{entry['date']} - {entry['product']}: {entry['qty']} unidades ({entry['reason']})", bg=self.branco)
            entry_info.pack(anchor="w", padx=10)

        # Alertas de Estoque
        alerts_frame = tk.Frame(self.main_frame, bg=self.branco)
        alerts_frame.grid(row=4, column=0, padx=10, pady=10)
        title = tk.Label(alerts_frame, text="Alertas de Estoque", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        alert = tk.Label(alerts_frame, text="Produto B está esgotado!", font=("Arial", 12), bg=self.branco, fg="red")
        alert.pack(anchor="w", padx=10)

        # Pesquisa de Produtos no Estoque
        search_frame = tk.Frame(self.main_frame, bg=self.branco)
        search_frame.grid(row=0, column=2, padx=10, pady=10)
        title = tk.Label(search_frame, text="Pesquisar Produto", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        search_entry = tk.Entry(search_frame, font=("Arial", 12), bg=self.cinza_claro)
        search_entry.pack(anchor="w", padx=10, pady=5)

    def show_cashier(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Caixa", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        cashier_placeholder = tk.Label(self.main_frame, text="Aqui será mostrado o status do caixa.", font=("Arial", 14), bg=self.branco)
        cashier_placeholder.grid(row=1, column=0, padx=10, pady=10)

    def show_sellers(self):
        self.clear_main_frame()
        title = tk.Label(self.main_frame, text="Vendedores", font=("Arial", 18), bg=self.cinza_claro)
        title.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.create_sellers_list()

    # Componentes do Dashboard
    def create_sales_graph(self):
        grafico_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        grafico_frame.grid(row=1, column=0, padx=10, pady=10)
        title = tk.Label(grafico_frame, text="Vendas", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        graph_placeholder = tk.Label(grafico_frame, text="Gráfico de Vendas", bg=self.branco, width=40, height=8)
        graph_placeholder.pack(padx=10, pady=10)

    def create_categories(self):
        categorias_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        categorias_frame.grid(row=1, column=1, padx=10, pady=10)
        title = tk.Label(categorias_frame, text="Categorias", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        categories_placeholder = tk.Label(categorias_frame, text="Gráfico de Categorias", bg=self.branco, width=40, height=8)
        categories_placeholder.pack(padx=10, pady=10)

    def create_stock_numbers(self):
        numeros_estoque_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        numeros_estoque_frame.grid(row=1, column=2, padx=10, pady=10)
        title = tk.Label(numeros_estoque_frame, text="Números do Estoque", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        stock_numbers_placeholder = tk.Label(numeros_estoque_frame, text="Total de itens e valor", bg=self.branco, width=40, height=8)
        stock_numbers_placeholder.pack(padx=10, pady=10)

    def create_orders_frame(self):
        pedidos_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        pedidos_frame.grid(row=1, column=3, padx=10, pady=10)
        title = tk.Label(pedidos_frame, text="Pedidos", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        orders_placeholder = tk.Label(pedidos_frame, text="Lista de pedidos", bg=self.branco, width=40, height=8)
        orders_placeholder.pack(padx=10, pady=10

    def create_orders_frame(self):
        pedidos_frame = tk.Frame(self.main_frame, bg=self.branco, width=350, height=200)
        pedidos_frame.grid(row=1, column=3, padx=10, pady=10)
        title = tk.Label(pedidos_frame, text="Pedidos", font=("Arial", 14), bg=self.branco)
        title.pack(anchor="w", padx=10, pady=5)
        orders_placeholder = tk.Label(pedidos_frame, text="Lista de pedidos", bg=self.branco, width=40, height=8)
        orders_placeholder.pack(padx=10, pady=10)

    def create_orders_frame(self):
        pedidos_frame = tk.Frame(self.main_frame, bg=self.branco, width=700, height=100)
        pedidos_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
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

        # Lista de produtos precisa colocar codigo de banco de dados
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

            image = tk.Label(product_frame, text="📦", bg=self.branco, width=10, height=5)
            image.grid(row=0, column=0, padx=10, pady=10)

            name_label = tk.Label(product_frame, text=product["name"], font=("Arial", 14), bg=self.branco)
            name_label.grid(row=1, column=0, padx=10)

            stock_price_label = tk.Label(product_frame, text=f"Estoque: {product['stock']} - R$ {product['price']:.2f}", bg=self.branco)
            stock_price_label.grid(row=2, column=0, padx=10)

            btn_info = tk.Button(product_frame, text="Mais Informações", bg=self.roxo, fg=self.branco)
            btn_info.grid(row=3, column=0, padx=10)

            btn_add_cart = tk.Button(product_frame, text="Adicionar ao Carrinho", bg=self.roxo, fg=self.branco)
            btn_add_cart.grid(row=4, column=0, padx=10)

            col += 1
            if col == max_columns:
                col = 0
                row += 1

    def create_sellers_list(self):
        sellers_frame = tk.Frame(self.main_frame, bg=self.cinza_claro, width=700)
        sellers_frame.grid(row=1, column=0, padx=200, pady=10, sticky="nsew")
        
        sellers = [
            {"name": "Vendedor 1", "id": "001"},
            {"name": "Vendedor 2", "id": "002"},
            {"name": "Vendedor 3", "id": "003"},
        ]

        for seller in sellers:
            # Card para cada vendedor - CUIDADO AO MEXER!!!!!!!
            seller_frame = tk.Frame(sellers_frame, bg=self.branco, bd=2, relief="groove", padx=20, pady=10)
            seller_frame.pack(padx=10, pady=10, fill="x")

            name_label = tk.Label(seller_frame, text=seller["name"], font=("Arial", 16, "bold"), bg=self.branco, fg=self.roxo)
            name_label.grid(row=0, column=0, padx=10, sticky="w")

            id_label = tk.Label(seller_frame, text=f"ID: {seller['id']}", font=("Arial", 12), bg=self.branco, fg=self.cinza_texto)
            id_label.grid(row=1, column=0, padx=10, sticky="w")

            label = tk.Button(seller_frame, text="|", bg="white", fg="white",borderwidth=0)
            label.grid(row=0, column=1, padx=200, sticky="e")

            btn_editar = tk.Button(seller_frame, text="📝", bg=self.cinza_claro, fg="blue", borderwidth=0, font=("Arial", 12))
            btn_editar.grid(row=0, column=1, padx=10, sticky="e")

            btn_delete = tk.Button(seller_frame, text="🗑️", bg="red", fg=self.branco, borderwidth=0, font=("Arial", 12))
            btn_delete.grid(row=0, column=2, padx=10, sticky="e")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipal(root)
    root.mainloop()
