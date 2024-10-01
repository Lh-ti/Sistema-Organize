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

label_cargo = tk.Label(janela, text="Cargo:")
label_cargo.grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_cargo = tk.Entry(janela)
entry_cargo.grid(row=2, column=1, padx=10, pady=5)

label_departamento = tk.Label(janela, text="Departamento:")
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
botao_salvar.grid(row=6, columnspan=2, pady=11)

janela.mainloop()
