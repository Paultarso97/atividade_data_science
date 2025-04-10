import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, Text, END, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def carregar_dados():
    try:
        df = pd.read_csv('dados.csv')
        df = df.dropna()
        df = df.drop_duplicates()
        return df
    except Exception as e:
        messagebox.showerror("Erro ao carregar dados", str(e))
        return pd.DataFrame()


def media():
    limpar_display()

    if dados.empty or 'vendas' not in dados.columns:
        messagebox.showwarning("Erro", "Dados ausentes ou coluna 'vendas' não encontrada.")
        return

    media_valor = np.mean(dados['vendas'])

    label_media = Label(display_frame, text=f"MÉDIA DAS VENDAS: {media_valor:.2f}", font=('Arial', 20, 'bold'))
    label_media.pack(pady=20)

def mediana():
    limpar_display()

    if dados.empty or 'vendas' not in dados.columns:
        messagebox.showwarning("Erro", "Dados ausentes ou coluna 'vendas' não encontrada.")
        return

    mediana_valor = np.median(dados['vendas'])

    label_mediana = Label(display_frame, text=f"MEDIANA DAS VENDAS: {mediana_valor:.2f}", font=('Arial', 20, 'bold'))
    label_mediana.pack(pady=20)


def calcular_moda():
    limpar_display()

    if dados.empty or 'vendas' not in dados.columns:
        messagebox.showwarning("Erro", "Dados ausentes ou coluna 'vendas' não encontrada.")
        return

    frequencias = dados['vendas'].value_counts()
    maior_freq = frequencias.max()
    modas = frequencias[frequencias == maior_freq].index.tolist()

    if len(modas) == len(frequencias):
        texto = "NÃO HÁ MODA (todos os valores aparecem com a mesma frequência)."
    else:
        texto = f"MODA(S) DAS VENDAS: {', '.join(map(str, modas))}"

    label_moda = Label(display_frame, text=texto, font=('Arial', 18, 'bold'))
    label_moda.pack(pady=20)

def mostrar_grafico():
    limpar_display()

    if dados.empty:
        messagebox.showwarning("ATENÇÃO", 'Não existem dados.')
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    if 'vendedor' in dados.columns and 'vendas' in dados.columns:
        dados.groupby('vendedor')['vendas'].sum().plot(kind='bar', ax=ax)
        ax.set_title('Vendas por Vendedor')
        ax.set_ylabel("Valor (R$)")
        ax.tick_params(axis='x', rotation=45)
    else:
        messagebox.showerror("Erro", "As colunas 'vendas' e 'vendedor' não foram encontradas.")
        return

    canvas = FigureCanvasTkAgg(fig, master=display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def grafico_setores():
    limpar_display()

    if dados.empty or 'vendas' not in dados.columns or 'vendedor' not in dados.columns:
        messagebox.showwarning("Erro", "Dados ausentes ou colunas 'vendas' e 'vendedor' não encontradas.")
        return

    fig, ax = plt.subplots(figsize=(7, 7))

    vendas_por_vendedor = dados.groupby('vendedor')['vendas'].sum()
    ax.pie(vendas_por_vendedor, labels=vendas_por_vendedor.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Participação de Vendas por Vendedor')
    ax.axis('equal')  # mantém o gráfico circular

    canvas = FigureCanvasTkAgg(fig, master=display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def limpar_display():
    for widget in display_frame.winfo_children():
        widget.destroy()


# Carregar dados
dados = carregar_dados()

# Criar janela
root = tk.Tk()
root.title("ANÁLISE DE DADOS")
root.geometry("800x600")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill='both', expand=True)

label = ttk.Label(main_frame, text="Análise de Dados", font=('Arial', 16))
label.pack()

btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Gráfico", command=mostrar_grafico).pack(side="left", padx=2)
ttk.Button(btn_frame, text="Setores", command=grafico_setores).pack(side="left", padx=3)
ttk.Button(btn_frame, text="Média", command=media).pack(side="left", padx=4)
ttk.Button(btn_frame, text="Mediana", command=mediana).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Moda", command=calcular_moda).pack(side="left", padx=6)
ttk.Button(btn_frame, text="Limpar", command=limpar_display).pack(side="left", padx=7)

display_frame = ttk.Frame(main_frame)
display_frame.pack(fill='both', expand=True)

root.mainloop()
