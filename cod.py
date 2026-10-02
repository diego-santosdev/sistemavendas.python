# ==========================================
# 1. IMPORTAÇÃO DE BIBLIOTECAS
# ==========================================
# 'streamlit' (apelidado de st) é usado para criar a interface web (textos, botões, gráficos).
import streamlit as st

# 'pandas' (apelidado de pd) é usado para manipulação e análise de dados (trabalhar com tabelas).
import pandas as pd

# 'plotly.express' (apelidado de px) é usado para criar gráficos interativos.
import plotly.express as px

# ==========================================
# 2. CARREGAMENTO DOS DADOS
# ==========================================
# Lê o arquivo 'vendas.csv' e o transforma em um DataFrame (tabela) do pandas.
tabela_vendas = pd.read_csv('vendas.csv')

# Exibe o título principal na tela central do aplicativo.
st.write('## SISTEMA DE VENDAS')

# ==========================================
# 3. MENU LATERAL (SIDEBAR) - FORMULÁRIO DE CADASTRO
# ==========================================
# Cria um título na barra lateral esquerda.
st.sidebar.write('## CADASTRAR VENDAS')

# Cria os campos de entrada de dados na barra lateral:
data = st.sidebar.date_input('Data') # Campo para selecionar uma data (calendário)
vendedor = st.sidebar.selectbox('Vendedor', ['Bruno', 'Ana', 'Carla']) # Menu suspenso com opções de vendedores
produto = st.sidebar.selectbox('Produto', ['Celular', 'Notebook', 'Fone']) # Menu suspenso com opções de produtos
quantidade = st.sidebar.number_input('Quantidade', step=1) # Campo para digitar números (step=1 garante números inteiros)
valor = st.sidebar.number_input('Valor') # Campo para digitar o valor (aceita decimais)

# Cria o botão que o usuário vai clicar para registrar a venda.
botao_cadastrar = st.sidebar.button('Cadastrar Produto')

# ==========================================
# 4. LÓGICA DE CADASTRO (SALVAR DADOS)
# ==========================================
# O bloco abaixo só é executado SE o botão 'Cadastrar Produto' for clicado.
if botao_cadastrar:
    # 4.1. Junta os dados preenchidos em uma lista (transformando a data em texto).
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    
    # 4.2. Descobre qual é o índice da última linha vazia da tabela atual.
    ultima_linha = len(tabela_vendas)
    
    # 4.3. Adiciona a lista 'nova_venda' nessa nova linha da tabela.
    tabela_vendas.loc[ultima_linha] = nova_venda
    
    # 4.4. Salva a tabela atualizada de volta no arquivo 'vendas.csv'.
    # O 'index=False' impede que o pandas crie uma coluna extra com os números das linhas.
    tabela_vendas.to_csv('vendas.csv', index=False)
    
    # 4.5. Mostra uma mensagem verde de sucesso na tela.
    st.success('Venda Cadastrada Com Sucesso!')

# ==========================================
# 5. VISUALIZAÇÃO DA TABELA
# ==========================================
st.write('## VENDAS CADASTRADAS')
# Mostra a tabela completa (DataFrame) na tela central para o usuário ver os dados.
st.dataframe(tabela_vendas)

# ==========================================
# 6. DASHBOARD (MÉTRICAS E GRÁFICOS)
# ==========================================
st.write('## Dashboard')

# --- MÉTRICA: Faturamento Total ---
# Soma todos os valores numéricos da coluna 'valor' da tabela.
faturamento = tabela_vendas['valor'].sum()
# Exibe um "card" bonito com o título e o valor total formatado com "R$".
st.metric('Faturamento Total', f'R${faturamento}')

# --- GRÁFICO 1: Barras (Venda por Vendedor) ---
# Cria um gráfico de barras onde o Eixo X é o vendedor, o Eixo Y é o valor, 
# e a cor de cada pedaço da barra representa o produto vendido.
grafico1 = px.bar(tabela_vendas, x='vendedor', y='valor', color='produto')
# Plota o gráfico na tela do Streamlit.
st.plotly_chart(grafico1)

# --- GRÁFICO 2: Pizza/Donut (Venda por Produto) ---
# Cria um gráfico de pizza. 'names' define as fatias (produtos) e 'values' o tamanho delas (valor).
# O parâmetro 'hole=0.5' faz um buraco no meio, transformando a pizza em um gráfico de rosca (donut).
grafico2 = px.pie(tabela_vendas, names='produto', values='valor', hole=0.5)
# Plota o gráfico na tela do Streamlit.
st.plotly_chart(grafico2)
