
from funcoes import *
from dic_produtos import produtos

valores_produtos = [preco for preco in produtos.values()]

def exibir_estatisticas(valores):
    print("Estatísticas dos Produtos:")
    print(f"Média: {calc_media(valores):.2f}")
    print(f"Mediana: {calc_mediana(valores):.2f}")
    print(f"Moda: {calc_moda(valores):.2f}")
    print(f"Amplitude: {calc_amplitude(valores):.2f}")
    print(f"Desvio Padrão: {calc_desvio_padrao(valores):.2f}")

if __name__ == "__main__":
    exibir_estatisticas(valores_produtos)


print(f'''

1) Qual é a diferença entre média e mediana?
RESPOSTA:
A média, assim como a mediana, é uma medida de tendência central, mas com papéis diferentes.
A média tem o papel de mostrar qual é a divisão igualitária entre a soma dos valores por cada
       um dos elementos do grupo analisado. Já a mediana tem como fundamento verificar qual dado
       está exatamente no meio do grupo, após colocar os valores em ordem crescente ou decrescente.

2) Por que a moda é importante?
RESPOSTA:
A moda mostra qual elemento mais apareceu. Se for fazer um sorteio, provavelmente vai cair na moda.
Se for no caso de vendas de produtos, ela vai mostrar qual o valor que as pessoas estão dispostas a
gastar ou ainda qual produto mais vendeu.

3) Qual é o significado da variância?
RESPOSTA:
A variância é uma normalização de dados e tem como objetivo calcular o quão distantes os dados estão
da média, elevado ao quadrado, para deixar os valores positivos (já que não existe distância negativa).
E dimensionar o quão dispersos os dados estão da média.

4) Como o desvio padrão relaciona-se com a variância?
RESPOSTA:
O desvio padrão é a raiz quadrada da variância.

''')