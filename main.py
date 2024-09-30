import tkinter as tk
from tkinter import messagebox, ttk

produtos_cadastrados = []

def mostrar_tabela():
    janela_tabela = tk.Toplevel()
    janela_tabela.title("Produtos Cadastrados")
    janela_tabela.geometry("900x300")
    
    colunas = ("id", "Nome", "Categoria", "Preço", "Quantidade")
    tree = ttk.Treeview(janela_tabela, columns=colunas, show="headings")
    
    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, anchor='center', minwidth=100, width=180)
    
    for produto in produtos_cadastrados:
        tree.insert("", tk.END, values=produto)
    
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def cadastrar_produto():
    id = entry_id.get()
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    preco = entry_preco.get()
    quantidade = entry_quantidade.get()

    aceita_termos = check_termos_var.get()
    
    if id and nome and categoria and preco and quantidade:
        try:
            id = int(id)
            preco = float(preco)
            quantidade = int(quantidade)

            if aceita_termos:
                if any(produto[0] == id for produto in produtos_cadastrados):
                    messagebox.showerror("Erro", "ID deve ser único!")
                    return

                produto = (id, nome, categoria, preco, quantidade)
                produtos_cadastrados.append(produto)
                
                entry_id.delete(0, tk.END)
                entry_nome.delete(0, tk.END)
                entry_categoria.delete(0, tk.END)
                entry_preco.delete(0, tk.END)
                entry_quantidade.delete(0, tk.END)

                messagebox.showinfo("Cadastro Concluído", "Produto cadastrado com sucesso!")
                mostrar_tabela()
                
            else:
                messagebox.showwarning("Erro", "Você deve aceitar os termos para continuar.")
        except ValueError:
            messagebox.showerror("Erro", "ID, preço e quantidade devem ser valores numéricos!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro de Produtos")
janela.geometry("400x450")

# Labels e Entradas
label_id = tk.Label(janela, text="ID do Produto:")
label_id.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_id = tk.Entry(janela)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(janela, text="Nome do Produto:")
label_nome.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_categoria = tk.Label(janela, text="Categoria:")
label_categoria.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=2, column=1, padx=10, pady=5)

label_preco = tk.Label(janela, text="Preço:")
label_preco.grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_preco = tk.Entry(janela)
entry_preco.grid(row=3, column=1, padx=10, pady=5)

label_quantidade = tk.Label(janela, text="Quantidade:")
label_quantidade.grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=4, column=1, padx=10, pady=5)

check_termos_var = tk.BooleanVar()
check_termos = tk.Checkbutton(janela, text="Aceito os Termos de Serviço", variable=check_termos_var)
check_termos.grid(row=5, columnspan=2, pady=10)

botao_salvar = tk.Button(janela, text="Salvar", command=cadastrar_produto)
botao_salvar.grid(row=6, columnspan=2, pady=10)

janela.mainloop()




import tkinter as tk
from tkinter import messagebox, ttk

funcionarios_cadastrados = []

def mostrar_tabela():
    janela_tabela = tk.Toplevel()
    janela_tabela.title("CADASTRAR FUNCIONÁRIOS")
    janela_tabela.geometry("900x300")
    
    colunas = ("id", "Nome", "Cargo", "Departamento", "Salário")
    tree = ttk.Treeview(janela_tabela, columns=colunas, show="headings")
    
    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, anchor='center', minwidth=100, width=180)
    
    for funcionario in funcionarios_cadastrados:
        tree.insert("", tk.END, values=funcionario)
    
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def cadastrar_funcionario():
    id = entry_id.get()
    nome = entry_nome.get()
    cargo = entry_cargo.get()
    departamento = entry_departamento.get()
    salario = entry_salario.get()

    aceita_termos = check_termos_var.get()
    
    if id and nome and cargo and departamento and salario:
        try:
            id = int(id)
            salario = float(salario)
            cargo = float(cargo)

            if aceita_termos:
                # Verifica se o ID é único
                if any(funcionario[0] == id for funcionario in funcionarios_cadastrados):
                    messagebox.showerror("Erro", "ID deve ser único!")
                    return

                funcionario = (id, nome, cargo, departamento, salario)
                funcionarios_cadastrados.append(funcionario)
                
                entry_id.delete(0, tk.END)
                entry_nome.delete(0, tk.END)
                entry_cargo.delete(0, tk.END)
                entry_departamento.delete(0, tk.END)
                entry_salario.delete(0, tk.END)

                messagebox.showinfo("Cadastro Concluído", "Funcionário cadastrado com sucesso!")
                mostrar_tabela()
                
            else:
                messagebox.showwarning("Erro", "Você deve aceitar os termos para continuar.")
        except ValueError:
            messagebox.showerror("Erro", "ID e salário devem ser valores numéricos!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro de Funcionários")
janela.geometry("400x450")

# Labels e Entradas
label_id = tk.Label(janela, text="ID:")
label_id.grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_id = tk.Entry(janela)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_cargo = tk.Label(janela, text="Descrição:")
label_cargo.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_cargo = tk.Entry(janela)
entry_cargo.grid(row=2, column=1, padx=10, pady=5)

label_departamento = tk.Label(janela, text="departamento:")
label_departamento.grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_departamento = tk.Entry(janela)
entry_departamento.grid(row=3, column=1, padx=10, pady=5)

label_salario = tk.Label(janela, text="Salário:")
label_salario.grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_salario = tk.Entry(janela)
entry_salario.grid(row=4, column=1, padx=10, pady=5)

check_termos_var = tk.BooleanVar()
check_termos = tk.Checkbutton(janela, text="Aceito os Termos de Serviço", variable=check_termos_var)
check_termos.grid(row=5, columnspan=2, pady=10)

botao_salvar = tk.Button(janela, text="Salvar", command=cadastrar_funcionario)
botao_salvar.grid(row=6, columnspan=2, pady=10)

janela.mainloop()
