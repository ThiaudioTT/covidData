import pandas as pd
import plotly.express as px
import streamlit as st


#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.selectbox("Select an state from Brazil", estados)

#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.selectbox("What type of data?", colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]


fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.plotly_chart(fig)
