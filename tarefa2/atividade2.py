
import pandas as pd
import matplotlib.pyplot as plt

# Carregar e limpar os dados
df = pd.read_csv('dados.csv')
df = df.dropna()
df = df.drop_duplicates()

# Funções de gráfico
def grafico_linha():
    plt.plot(df['Mês'], df['Vendas'])
    plt.title('Vendas ao longo do tempo')
    plt.xlabel('Meses')
    plt.ylabel('Vendas')  
    plt.tight_layout()
    plt.show()

def grafico_pizza():
    rotulos = df['Mês']
    valores = df['Vendas']
    plt.pie(valores, labels=rotulos, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição de Vendas por Categoria')
    plt.axis('equal')  
    plt.show()

def grafico_barras():
    plt.bar(df['Mês'], df['Vendas'])  
    plt.title('Vendas ao longo do tempo')
    plt.xlabel('Meses')
    plt.ylabel('Vendas')  
    plt.tight_layout()
    plt.show()

def grafico_dispercao():
    plt.scatter(df['Mês'], df['Vendas']) 
    plt.title('Vendas ao longo do tempo')
    plt.xlabel('Meses')
    plt.ylabel('Vendas') 
    plt.tight_layout()
    plt.show()

# Loop de escolha do gráfico
while True:
    print("\nEscolha o tipo de gráfico:")
    print("1 - Gráfico de Linha")
    print("2 - Gráfico de Pizza")
    print("3 - Gráfico de Barras")
    print("4 - Gráfico de Dispersão")
    print("0 - Sair")

    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        grafico_linha()
    elif escolha == '2':
        grafico_pizza()
    elif escolha == '3':
        grafico_barras()
    elif escolha == '4':
        grafico_dispercao()
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
