

#interface
import streamlit as st
#dados
import pandas as pd
#gráfico
import plotly.express as px

#carregar a base de vendas
tabela_vendas=pd.read_csv('vendas.csv')

st.write('## SISTEMA DE VENDAS')

#Cadastro de vendas
st.sidebar.write('## CADASTRAR VENDAS')

data=st.sidebar.date_input('Data')
vendedor=st.sidebar.selectbox('Vendedor',['Bruno','Ana','Carla'])
produto=st.sidebar.selectbox('produto', ['Celular','Notebook', 'Fone'])
quantidade=st.sidebar.number_input('Quantidade',step=1)
valor=st.sidebar.number_input('Valor')
botao_cadastrar=st.sidebar.button('Cadastrar Produto')

#lógica de cadastro

if botao_cadastrar:
    nova_venda=[str(data),vendedor,produto,quantidade,valor]
    ultima_linha= len (tabela_vendas)
    tabela_vendas.loc[ultima_linha]=nova_venda
    tabela_vendas.to_csv('vendas.csv', index=False)
    st.success('Venda Cadastrada Com Sucesso!')


#visualizar vendas
st.write('## VENDAS CADASTRADAS')
st.dataframe(tabela_vendas)


#dashboard
st.write('## Dashboard')

#card/métrtica-> faturamento
faturamento=tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R${faturamento}')

#gráfico de barras/ coluna ->venda por vendedor
grafico1=px.bar(tabela_vendas, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico1)

#gráfico de pizza -> venda por produto
grafico2=px.pie(tabela_vendas, names='produto', values='valor',hole=0.5)
st.plotly_chart(grafico2)